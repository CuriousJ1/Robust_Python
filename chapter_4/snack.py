from dataclasses import dataclass
# If you aren't familiar with data classes, you'll learn more in chapter 10
# but for now, treat this as four fields grouped together and what types they are

# version 1.
@dataclass
class Snack:
    name: str
    condiments: set[str]
    error_code: int
    disposed_of: bool

Snack("Hotdog", {"Mustard", "Ketchup"}, 5, False)

# version 2.
@dataclass
class Error:
    error_code: int
    disposed_of: bool


@dataclass
class Snack: name: str


condiments: set[str]
snack: Union[Snack, Error] = Snack("Hotdog", {"Mustard", "Ketchup"})
snack = Error(5, True)