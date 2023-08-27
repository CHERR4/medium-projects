from typing import List
from numbers import Number
from estimator.estimator import Estimator
from sklearn.metrics import mean_squared_error
import math


class Rmse(Estimator):

    def error(self, actual: List, predicted: List) -> Number:
        return math.sqrt(mean_squared_error(actual, predicted))        

    def is_better(self, actual_score: Number, new_score: Number) -> bool:
        return new_score < actual_score
