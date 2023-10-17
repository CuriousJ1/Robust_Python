
from pydantic.dataclasses import dataclass
from typing import Union


def double_or_square(x: Union[int, float]) -> Union[int, float]:
    if isinstance(x, int):
        return x * 2
    elif isinstance(x, float):
        return x * x

    raise ValueError("Double or Square only take in int or float values")

print(double_or_square(5))     # Returns 10 (int)
print(double_or_square(2.5))   # Returns 6.25 (float)
print(double_or_square("Hello"))