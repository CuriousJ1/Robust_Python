'''
Version 1.

Innocuosous reverse list function
How do I know that the returned list should contain the same type as the passed-in
list?

'''
def reverse(coll: list) -> list:
    return coll[::-1]

'''
Version 2.

This says for type T, reverse takes in a list of elements of type T and returns
a list of elements o type T.

I can't mix types: a list of integers will never be able to become a list of strings
if those lists aren't using the same TypeVar.

'''

from typing import TypeVar
T = TypeVar('T')
def reverse(coll: list[T]) -> list[T]:
    return coll[::-1]