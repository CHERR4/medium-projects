from typing import List

from annotated_types import T


def single(list: List[T]) -> T:
    if len(list) != 1:
        raise ValueError(
            f"Expected length 1, got list with length {len(list)}, value: {list}"
        )
    return list[0]


def defined(value: T | None) -> T:
    if not value:
        raise ValueError("Not null value expected")
    return value
