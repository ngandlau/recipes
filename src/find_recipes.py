from typing import List
from src.item import Item
from src.recipe import Recipe


def find_recipe_given_leftovers(leftovers: List[Item], recipes: List[Recipe]) -> List[Recipe]:
    """
    Finds recipes that can be made from the leftovers of `recipe`, or at least
    recipes that do not need many more ingredients.

    Returns a list of recipes that require at least *one* of the ingredients
    that is left over.
    """
    recipes_made_with_leftovers = []
    for recipe in recipes:
        ingredients = recipe.get_ingredients()

        n_common_ingredients = 0
        for item in leftovers:
            if item.ingredient in ingredients:
                n_common_ingredients += 1

        if n_common_ingredients > 0:
            recipes_made_with_leftovers.append((recipe, n_common_ingredients))

    # recipes are sorted by their number of common ingredients in descending order
    recipes_made_with_leftovers.sort(key=lambda i:i[1], reverse=True)

    return recipes_made_with_leftovers


        

