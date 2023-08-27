from typing import List

import pandas as pd
from grid.grid_response import GridResponse
from grid.grid_model import GridModel
from grid.model_response import ModelResponse
from estimator.estimator import Estimator


class GridSearch:


    def execute(self, time_series: pd.DataFrame, models: List[GridModel], estimator: Estimator, n_predict: int) -> GridResponse:
        grid_response = GridResponse(None, [], estimator)
        estimator = estimator()
        test = time_series.tail(n_predict)
        train = time_series.drop(test.index)
        test_values = test.values
        for model in models:
            print('Model:', model.name)
            grid_params = model.get_params_combinations()
            n_combinations = len(grid_params)
            print('Number of combinations:', n_combinations)
            i = 1
            for params in grid_params:
                instance = model.model(**params)
                instance.train(train)
                predicted = instance.predict(n_predict)
                error = estimator.error(test_values, predicted)
                response = ModelResponse(model.name, model.model, params, error, instance)
                grid_response.models.append(response)

                if not grid_response.best_model or estimator.is_better(grid_response.best_model.error, response.error):
                    grid_response.best_model = response

                print('Combination:', i, '/', n_combinations, 'RMSE:', error, 'best actual:', grid_response.best_model.error)
                i += 1
                
        return grid_response
                
