# Enumerations

Enumerations are simple, and often overlooked as a powerful communication method. Any time that you want to represent a single value from a static collection of values, an enumeration should be your go-to user-defined type. It’s easy to define and use them. They offer a wealth of operations, including iteration, bitwise operations (in the case of Flag enumerations), and control over uniqueness.
Remember these key limitations:
• Enumerations are not meant for dynamic key-value mappings that change at runtime. Use a dictionary for this.
• Flag enumerations only work with values that support bitwise operations with nonoverlapping values.
• Avoid IntEnum and IntFlag unless absolutely necessary for system interoperability.

Next up, I will explore another user-defined type: a dataclass. While enumerations are great at specifying a relationship about a set of values in just one variable, data classes define relationships between multiple variables.