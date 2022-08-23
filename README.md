# Medium projects
I will upload all my projects made to write medium articles: https://medium.com/@jramoncaserofuentes

## Live sentiment analysis Spark Flask

## Run
- `cd live-sentiment-analysis-spark-flask`
- `python3 -m venv .plot-twitter-spark-env` (This step is recommended to install dependencies in a clean environment)
- `source .plot-twitter-spark-env/bin/activate`
- `pip3 install -r requirements.txt`   
**Open three Terminals and run in this orden**
- `python src/tweets_listener.py`
- `python src/spark_client.py`
- `python src/api.py`