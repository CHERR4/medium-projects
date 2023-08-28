from typing import List
from grid.grid_response import GridResponse
from grid.grid_model import GridModel
from grid.model_response import ModelResponse
from estimator.estimator import Estimator
import pandas as pd


class GridSearch:
    time_series: pd.DataFrame
    models: List[GridModel]
    estimator: Estimator
    n_predict: int

    def __init__(self, time_series: pd.DataFrame, models: List[GridModel], estimator: Estimator, n_predict: int):
        self.time_series = time_series
        self.models = models
        self.estimator = estimator
        self.n_predict = n_predict


    def execute(self) -> GridResponse:
        grid_response = GridResponse(None, [], self.estimator)
        estimator = self.estimator()
        test = self.time_series.tail(self.n_predict)
        train = self.time_series.drop(test.index)
        test_values = test.values
        for model in self.models:
            print('Model:', model.name)
            grid_params = model.get_params_combinations()
            n_combinations = len(grid_params)
            print('Number of combinations:', n_combinations)
            i = 1
            for params in grid_params:
                instance = model.model(**params)
                instance.train(train)
                predicted = instance.predict(self.n_predict)
                error = estimator.error(test_values, predicted)
                response = ModelResponse(model.name, model.model, params, error, instance)
                grid_response.models.append(response)

                if not grid_response.best_model or estimator.is_better(grid_response.best_model.error, response.error):
                    grid_response.best_model = response

                print('Combination:', i, '/', n_combinations, 'RMSE:', error, 'best actual:', grid_response.best_model.error)
                i += 1
                
        return grid_response
