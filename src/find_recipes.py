from typing import List
from src.recipe import Recipe


def find_recipe_given_leftovers(recipe: Recipe, recipes: List[Recipe]) -> List[Recipe]:
    """
    Finds recipes that can be made from the leftovers of `recipe`, or at least
    recipes that do not need many more ingredients.

    Returns a list of recipes that require at least *one* of the ingredients
    that is left over.
    """
    leftovers = recipe.leftovers()
    leftover_ingredients = [ingredient for ingredient, amount, unit in leftovers]

    partner_recipes = []
    for other_recipe in recipes:
        if recipe == other_recipe:
            continue

        n_common_ingredients = 0
        for ingredient in leftover_ingredients:
            if ingredient in other_recipe.ingredients:
                n_common_ingredients += 1

        if n_common_ingredients > 0:
            partner_recipes.append((other_recipe, n_common_ingredients))

    return partner_recipes


        

