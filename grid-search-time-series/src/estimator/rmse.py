from typing import List
from numbers import Number
from estimator.estimator import Estimator
from sklearn.metrics import mean_squared_error
import math
import numpy as np


class Rmse(Estimator):

    def flatten_concatenation(self, matrix: List[List]):
        flat_list = []
        for row in matrix:
            flat_list += row
        return flat_list

    def error(self, actual: List, predicted: List) -> Number:
        print(predicted)
        return math.sqrt(mean_squared_error(actual, predicted))        

    def is_better(self, actual_score: Number, new_score: Number) -> bool:
        return new_score < actual_score
