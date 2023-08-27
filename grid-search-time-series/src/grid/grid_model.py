from model.time_series_model import TimeSeriesModel
from typing import Dict, List


class GridModel:

    name: str
    model: TimeSeriesModel
    params_grid: Dict

    def __init__(self, name: str, model: TimeSeriesModel, params_grid: Dict):
        self.name = name
        self.model = model
        self.params_grid = params_grid


    def __add_combinations_from_list(self, combinations: List[Dict], key: str, values: List) -> List[Dict]:
        new_combinations = []
        if not combinations:
            for value in values:
                new_dict = {key: value}
                new_combinations.append(new_dict)
            return new_combinations
        
        for dictionary in combinations:
            for value in values:
                new_dict = dict(dictionary)
                new_dict[key] = value
                new_combinations.append(new_dict)
        return new_combinations


    def get_params_combinations(self) -> List[Dict]:
        combinations = []
        params_keys = self.params_grid.keys()
        for key in params_keys:
            combinations = self.__add_combinations_from_list(combinations, key, self.params_grid[key])
        return combinations
