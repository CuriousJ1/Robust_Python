from typing import Literal
from dataclasses import dataclass
@dataclass
class Error:
    error_code: Literal[1,2,3,4,5]
    disposed_of: bool
@dataclass
class Snack:
    name: Literal["Pretzel", "Hot Dog", "Veggie Burger"]
    condiments: set[Literal["Mustard", "Ketchup"]]

error_instance = Error(0, False)


snack_invalid = Snack("Invalid", set())
snack_valid = Snack("Pretzel", {"Mustard", "Relish"})

print(error_instance)
print(snack_invalid)
print(snack_valid)