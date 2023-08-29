'''
Version 1.


'''
def adjust_recipe(recipe, servings):
    """
        Take a meal recipe and change the number of servings
        :param recipe: A list, where the first element is the number of servings,
                       and the remainder of elements follow the (name, amount, unit)
                       format, such as ("flour", 1.5, "cup")
        :param servings: the number of servings
        :return list: a new list of ingredients, where the first element is the
                      number of servings
    """
    new_recipe = [servings]
    old_servings = recipe[0]
    factor = servings / old_servings
    recipe.pop(0)

    while recipe:
        ingredient, amount, unit = recipe.pop(0)
        #please only use numbers that will be easily measurable
        new_recipe.append((ingredient, amount * factor, unit))

    return new_recipe


'''
Version 2.


'''

Ingredient = tuple[str, int, str] # (name, quantity, units)
Recipe = list[Union[int, Ingredient]] # the list can be servings or ingredients
def adjust_recipe(recipe: Recipe, servings):
# ...