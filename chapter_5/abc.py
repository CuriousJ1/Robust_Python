'''
Version 1.

Let’s look at a collections.abc.Set, since there is no UserSet elsewhere in collec‐ tions.
I want to create a custom set that automatically handles aliases of ingredients
(such as rocket and arugula). In order to create this custom set, I need to implement
three methods, as required by collections.abc.Set:

__contains__
This is for membership checks: "arugula" in ingredients.

__iter__
This is for iterating: for ingredient in ingredients.

__len__
This is for checking the length: len(ingredients).

'''
import collections
class AliasedIngredients(collections.abc.Set):
    def __init__(self, ingredients: set[str]):
        self.ingredients = ingredients
    def __contains__(self, value: str):
        return value in self.ingredients or any(alias in self.ingredients
                                        for alias in get_aliases(value))
    def __iter__(self):
        return iter(self.ingredients)
    def __len__(self):
        return len(self.ingredients)