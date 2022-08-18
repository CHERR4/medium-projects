from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SQLContext, Row
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


def get_sql_context_instance(spark_context) -> SQLContext:
    """Create sql context singleton
    """
    if 'sqlContextSingletonInstance' not in globals():
        globals()['sqlContextSingletonInstance'] = SQLContext(spark_context)
    return globals()['sqlContextSingletonInstance']


def send_df_to_dashboard(df) -> int:
    """Send hashtags and counts to flask api
    """
    top_tags = [str(t.hashtag) for t in df.select("hashtag").collect()]  # Get hashtags from DataFrame
    tags_count = [p.hashtag_count for p in df.select("hashtag_count").collect()]  # Get counts from DataFrame
    url = 'http://localhost:3000/update-data'  # Flask local app endpoint to update data
    request_data = {'label': str(top_tags), 'data': str(tags_count)}  # Request body
    response = requests.post(url, data=request_data)  # Send hashtags, counts to update data endpoint
    return response.status_code


def process_rdd(time, rdd):
    """Process each RDD
    """
    print("----------- %s -----------" % str(time))
    try:
        sql_context = get_sql_context_instance(rdd.context)  # Get Spark sql context (is singleton)
        row_rdd = rdd.map(lambda w: Row(hashtag=w[0], hashtag_count=w[1]))  # RDD to SQL RDD
        hashtags_df = sql_context.createDataFrame(row_rdd)  # SQL RDD to DataFrame
        hashtags_df.registerTempTable("hashtags")  # Register hashtags table
        # select ten more repeated hashtags (table hashtags)
        hashtag_counts_df = sql_context.sql(
            "select hashtag, hashtag_count from hashtags order by hashtag_count desc limit 10")
        hashtag_counts_df.show() # Print by screen, better for debugging
        send_df_to_dashboard(hashtag_counts_df)  # Send DataFrame to Dashboard (Flask App)
    except:
        e = sys.exc_info()[0]
        print("Error: %s" % e)


def setup():
    """Setup all Spark context and process
    """
    spark_context = SparkContext()  # Create Spark context
    spark_context.setLogLevel("ERROR")
    streaming_context = StreamingContext(spark_context, 2)  # Enable Streaming context and set batch size
    streaming_context.checkpoint("checkpoint_TwitterApp")  # Create checkpoint to make it fault-tolerance
    socket_stream = streaming_context.socketTextStream("127.0.0.1", 5557)  # Connect to Twitter's socket
    words = socket_stream.flatMap(lambda line: line.split(" "))  # Split text received in the socket
    hashtags = words.filter(lambda w: '#' in w).map(lambda x: (x, 1))  # Filter Hashtags
    tags_totals = hashtags.updateStateByKey(aggregate_tags_count)  # Apply function by key
    tags_totals.foreachRDD(process_rdd)  # Process each rdd with the process_rdd function
    streaming_context.start()  # Start transmission
    streaming_context.awaitTermination()  # Await until transmission ended by twitter client


if __name__ == "__main__": 
    setup()
