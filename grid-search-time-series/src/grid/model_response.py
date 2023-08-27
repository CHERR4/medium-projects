from src.model.time_series_model import TimeSeriesModel
from typing import Optional, Dict
from numbers import Number
from dataclasses import dataclass

@dataclass
class ModelResponse:
    name: str
    model: TimeSeriesModel
    params: Dict
    error: Number
    instance: Optional[TimeSeriesModel]

    