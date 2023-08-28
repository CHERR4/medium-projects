import pandas as pd


class TimeSeriesModel:

    def train(self, train_df: pd.DataFrame):
        raise NotImplementedError

    def predict(self, steps: int) -> list:
        raise NotImplementedError
    
