from typing import Literal

def greet(name: Literal["Alice", "Bob"]) -> str:
    return f"Hello, {name}!"

print(greet("Alice"))  # Valid
print(greet("Eve"))    # Type error, as "Eve" is not a valid argument