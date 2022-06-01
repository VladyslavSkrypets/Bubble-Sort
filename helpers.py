from random import randint
from functools import wraps
from time import perf_counter
from typing import Callable, List


def execution_timer(function: Callable):
    @wraps(function)
    def wrapper(*args, **kwargs):

        start_execution = perf_counter()

        result = function(*args, **kwargs)

        end_execution = perf_counter() - start_execution

        print(
            f'Function "{function.__name__}" sorted array with {len(kwargs["array"])} elements '
            f'in {round(end_execution * 1_000_000)} microseconds.'
        )

        return result
    return wrapper


def generate_array(length: int = 0) -> List[int]:
    left_num_limit, right_num_limit = -(length * length), length * length

    return [randint(left_num_limit, right_num_limit) for _ in range(length)]
