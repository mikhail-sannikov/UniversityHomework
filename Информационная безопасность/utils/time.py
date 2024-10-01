from time import perf_counter
from typing import Callable


def time_counter(func: Callable) -> Callable:
    def wrapper(*args: tuple, **kwargs: dict) -> tuple:
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()

        spent_time = end - start

        return result, spent_time

    return wrapper
