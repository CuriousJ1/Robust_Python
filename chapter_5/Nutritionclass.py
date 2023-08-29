'''
Version 1.

- The (dict) syntax indicates that we are subclassing from dictionaries.

- __getitem__ is what gets called when you use brackets to check a key in a dictio‐
nary: (nutrition["rocket"]) calls __getitem__(nutrition, "rocket").

- If a key is found, use the parent dictionary’s key check.

- For every alias, check if it is in the dictionary.

- Throw a KeyError if no key is found, either with what’s passed in or any of its aliases.

'''

class NutritionalInformation(dict):
    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except KeyError:
            pass

        for alias in get_aliases(key):
            try:
                return super().__getitem__(alias)
            except KeyError:
                pass

        raise KeyError(f"Could not find {key} or any of its aliases")

'''
Version 2. 

'''

from collections import UserDict
class NutritionalInformation(UserDict):
    def __getitem__(self, key):
        try:
            return self.data[key]
        except KeyError:
            pass

    for alias in get_aliases(key):
        try:
            return self.data[alias]
        except KeyError:
            pass

    raise KeyError(f"Could not find {key} or any of its aliases")