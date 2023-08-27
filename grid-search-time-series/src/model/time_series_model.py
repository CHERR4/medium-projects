import pandas as pd
from typing import Dict

class TimeSeriesModel:

    def train(self, train_df: pd.DataFrame):
        raise NotImplementedError

    def predict(self, steps: int) -> list:
        raise NotImplementedError
    
    def get_params(self) -> Dict:
        raise NotImplementedError
