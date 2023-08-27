from typing import List, Optional
from grid.model_response import ModelResponse
from estimator.estimator import Estimator
from dataclasses import dataclass


@dataclass
class GridResponse:
    best_model: ModelResponse
    models: Optional[List[ModelResponse]]
    estimator: Estimator
