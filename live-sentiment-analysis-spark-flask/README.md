# Plot Twitter's live data with Spark and Flask

## Run
- `python3 -m venv .plot-twitter-spark-env` (This step is recommended to install dependencies)
- `source .plot-twitter-spark-env/bin/activate`
- `pip3 install -r requirements.txt`
- `python src/tweets_listener.py`
- `python src/spark_client.py`
- `python src/api.py`