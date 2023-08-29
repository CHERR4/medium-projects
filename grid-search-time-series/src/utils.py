import pandas as pd
from typing import Tuple


def cluster_grouped_ts(dataset: pd.DataFrame, cluster_id: int) -> pd.DataFrame:
  cluster_series = dataset[dataset['cluster'] == cluster_id]
  cluster_series.drop(['id','cluster'], axis = 1, inplace = True)
  return cluster_series.groupby('datetime').sum()

def train_test_split(time_series: pd.DataFrame, n_test: int) -> Tuple[pd.DataFrame, pd.DataFrame]:
  test = time_series.tail(n_test)
  train = time_series.drop(test.index)
  return (train, test)