import pandas as pd


def cluster_grouped_ts(dataset: pd.DataFrame, cluster_id: int) -> pd.DataFrame:
  cluster_series = dataset[dataset['cluster'] == cluster_id]
  cluster_series.drop(['id','cluster'], axis = 1, inplace = True)
  return cluster_series.groupby('datetime').sum()