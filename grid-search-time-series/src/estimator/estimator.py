from typing import List
from numbers import Number

class Estimator:
    def error(self, actual: List[Number], predicted: List[Number]) -> Number:
        raise NotImplementedError
    
    def is_better(self, actual_score: Number, new_score: Number) -> bool:
        raise NotImplementedError