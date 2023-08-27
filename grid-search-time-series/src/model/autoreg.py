import pandas as pd
from typing import Any
from numbers import Number
from skforecast.ForecasterAutoreg import ForecasterAutoreg
from model.time_series_model import TimeSeriesModel



class Autoreg(TimeSeriesModel):
    regressor: Any
    random_state: int
    lags: int
    model: Any


    def __init__(self, regressor: Any, lags: int = 25, random_state: int = 0):
        self.regressor = regressor
        self.random_state = random_state
        self.lags = lags
        self.model = ForecasterAutoreg(regressor = regressor(random_state=random_state), lags=lags)

    def train(self, train_df: pd.DataFrame):
        self.model.fit(y=train_df['consumption'])

    def __zero_if_negative(self, value: Number) -> Number:
        if value < 0:
            return 0
        return value

    def predict(self, n_days: int):
        predictions = self.model.predict(n_days)
        predictions =  [self.__zero_if_negative(x) for x in predictions]
        return predictions
