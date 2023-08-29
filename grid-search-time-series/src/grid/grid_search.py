from typing import List
from grid.grid_response import GridResponse
from grid.grid_model import GridModel
from grid.model_response import ModelResponse
from estimator.estimator import Estimator
import pandas as pd


class GridSearch:
    train: pd.DataFrame
    test: pd.DataFrame
    models: List[GridModel]
    estimator: Estimator

    def __init__(self, train: pd.DataFrame, test: pd.DataFrame, models: List[GridModel], estimator: Estimator):
        self.train = train
        self.test = test
        self.models = models
        self.estimator = estimator


    def execute(self) -> GridResponse:
        grid_response = GridResponse(None, [], self.estimator)
        estimator = self.estimator()
        test_values = self.test.values
        n_predict = len(test_values)
        for model in self.models:
            print('Model:', model.name)
            grid_params = model.get_params_combinations()
            n_combinations = len(grid_params)
            print('Number of combinations:', n_combinations)
            i = 1
            for params in grid_params:
                instance = model.model(**params)
                instance.train(self.train)
                predicted = instance.predict(n_predict)
                error = estimator.error(test_values, predicted)
                response = ModelResponse(model.name, model.model, params, error, instance)
                grid_response.models.append(response)

                if not grid_response.best_model or estimator.is_better(grid_response.best_model.error, response.error):
                    grid_response.best_model = response

                print('Combination:', i, '/', n_combinations, 'RMSE:', error, 'best actual:', grid_response.best_model.error)
                i += 1
                
        return grid_response
