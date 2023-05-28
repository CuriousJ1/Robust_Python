# Version 1.
# Take a meal recipe and change the number of servings
# by adjusting each ingredient
# A recipe's first element is the number of servings, and the remainder # of elements is (name, amount, unit), such as ("flour", 1.5, "cup")
def adjust_recipe(recipe, servings):
    new_recipe = [servings]
    old_servings = recipe[0]
    factor = servings / old_servings
    recipe.pop(0)
    while recipe:
        ingredient, amount, unit = recipe.pop(0)
    # please only use numbers that will be easily measurable new_recipe.append((ingredient, amount * factor, unit))
    return new_recipe

#version 2
def adjust_recipe_1(recipe, servings):
    old_servings = recipe.pop(0)
    factor = servings / old_servings
    new_recipe_1 = {ingredient: (amount*factor, unit)
                    for ingredient, amount, unit in recipe}
    new_recipe_1["servings"] = servings
    return new_recipe_1