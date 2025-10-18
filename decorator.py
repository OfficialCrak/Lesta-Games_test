import time
from functools import wraps
from typing import Callable, Any


def time_it(func: Callable) -> Callable:
    """
    Декоратор для измерения вреиени выполнения функции.
    :param func:
    :return: result
    """

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f"Метод '{func.__name__}' выполнилась за {total_time * 1e6:.3f} мкс")
        return result

    return wrapper
