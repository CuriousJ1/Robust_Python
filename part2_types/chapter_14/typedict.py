from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

person_info: Person = {"name": "Alice", "age": 30}
big_bob: Person = {"name": "Bob", "age": 300}

# You can use type hints to specify that a variable should have the Person type.
def print_person_info(info: Person):
    print(f"Name: {info['name']}, Age: {info['age']}")

print_person_info(person_info)
print_person_info(big_bob)
