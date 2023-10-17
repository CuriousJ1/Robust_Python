from dataclasses import dataclass
from enum import auto, Enum

pat={
    "name": "",
    "years_experience": 0,
    "address": ""
    }
@dataclass
class Person():
    name: str = ""
    years_experience: int = 0
    address: str = ""