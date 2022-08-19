from dataclasses import dataclass
from enum import Enum, auto
from math import ceil
from typing import List

class Unit(Enum):
    mililiter = auto()
    essloeffel = auto()
    teeloeffel = auto()
    dose = auto()
    stueck = auto()

class Ingredient(Enum):
    gehackte_tomaten = auto()
    knoblauchzehe = auto()
    nudeln = auto()
    reis = auto()
    gegrillte_paprika =auto()
    kichererbsen = auto()

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
        amounts=[2.0, 0.5],
        units=[Unit.stueck, Unit.dose]
    )
    print(hummus_classic)
    print(hummus_classic.leftovers())
