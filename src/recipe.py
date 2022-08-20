from dataclasses import dataclass
from unit import Unit
from ingredient import Ingredient
from math import ceil
from typing import List

@dataclass
class Recipe:
    name: str
    ingredients: List[Ingredient]
    amounts: List[float]
    units: List[Unit]

    def leftovers(self):
        leftovers = []
        for ingredient, amount, unit in zip(self.ingredients, self.amounts, self.units):
            if not amount.is_integer():
                leftover_amount = ceil(amount) - amount
                leftovers.append((ingredient, leftover_amount, unit))
        return leftovers

def find_partner_recipes(Recipes):
    """
    Finds recipes that can be cooked together, because the leftovers of one
    recipe can be used for the other, and vice versa
    """
    return None

def recipe_similarity(recipe1, recipe2):
    """Calculates the similarity between two recipes"""
    # can the leftovers from recipe1 be used for recipe2?
    leftovers = recipe1.leftovers()
    used_leftovers = recipe2.what_leftovers_can_be_used_for_recipe(leftovers)
    waste = leftovers - used_leftovers

    # can the leftovers from recipe2 be used for recipe1?
    leftovers = recipe2.leftovers()
    used_leftovers = recipe1.what_leftovers_can_be_used_for_recipe(leftovers)
    waste = leftovers - used_leftovers
    return None

def find_recipe_given_leftovers(leftovers):
    """
    Finds recipes that can be made with the given leftovers, or at least
    recipes that do not need much more than what is left over.
    """
    return None



if __name__ == '__main__':
    hummus_classic = Recipe(
        name='Hummus',
        ingredients=[Ingredient.knoblauchzehe, Ingredient.kichererbsen],
        amounts=[2.0, 1.0],
        units=[Unit.stueck, Unit.dose]
    )
    print(hummus_classic)
    print(hummus_classic.leftovers())
