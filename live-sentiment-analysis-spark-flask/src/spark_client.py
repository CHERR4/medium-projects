from datetime import datetime
import json
import re
from pyspark.context import SparkContext
from pyspark.streaming import StreamingContext
from textblob import TextBlob
import requests
import sys


def aggregate_tags_count(new_values, total_sum):
    """Receive new values tuples and previous total_sum of key

    Args:
        new_values : new values of key
        total_sum : previous total_sum of key

    Returns:
        new total_sum of key
    """
    return sum(new_values) + (total_sum or 0)


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)

def send_polarity_to_dashboard(polarity, timestamp) -> int:
    """Send hashtags and counts to flask api
    """
    url = 'http://localhost:3000/update-polarity'  # Flask local app endpoint to update data
    request_data = {'polarity': polarity, 'timestamp': timestamp.isoformat()}
    print(request_data)
    response = requests.post(url, data=request_data)
    return response.status_code


def process_rdd(time, rdd):
    """Process each RDD
    """
    print("----------- %s -----------" % str(time))
    try:
        polarity = rdd.reduceByKey(lambda x,y: x + y).collect()[0][1]
        send_polarity_to_dashboard(polarity, time)  # Send DataFrame to Dashboard (Flask App)
    except Exception as error:
        print(error)
        e = sys.exc_info()[0]
        print("Error: %s" % e)


def polarity_detection(text):
    return TextBlob(text).sentiment.polarity


def preprocessing(line):
    line = re.sub(r'[.,"!]+', '', line, flags=re.MULTILINE)  # removes the characters specified
    line = re.sub(r'^RT[\s]+', '', line, flags=re.MULTILINE)  # removes RT
    line = re.sub(r'https?:\/\/.*[\r\n]*', '', line, flags=re.MULTILINE)  # remove link
    line = re.sub(r'[:]+', '', line, flags=re.MULTILINE)
    return line


def setup():
    """Setup all Spark context and process
    """
    spark_context = SparkContext()  # Create Spark context
    spark_context.setLogLevel("ERROR")
    streaming_context = StreamingContext(spark_context, 2)  # Enable Streaming context and set batch size
    streaming_context.checkpoint("checkpoint_TwitterApp")  # Create checkpoint to make it fault-tolerance
    lines = streaming_context.socketTextStream("127.0.0.1", 5557)  # Connect to Twitter's socket
    cleaned_lines = lines.map(preprocessing)
    sentiments = cleaned_lines.map(lambda x: (1, polarity_detection(x)))
    sentiments.foreachRDD(process_rdd)  # Process each rdd with the process_rdd function
    streaming_context.start()  # Start transmission
    streaming_context.awaitTermination()  # Await until transmission ended by twitter client


if __name__ == "__main__": 
    setup()
