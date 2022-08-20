from dataclasses import dataclass
from math import ceil
from typing import List, Tuple

from src.unit import Unit
from src.ingredient import Ingredient

@dataclass
class Recipe:
    name: str
    ingredients: List[Ingredient]
    amounts: List[float]
    units: List[Unit]

    def leftovers(self) -> List[Tuple[Ingredient, float, Unit]]:
        leftovers = []
        for ingredient, amount, unit in zip(self.ingredients, self.amounts, self.units):
            if not amount.is_integer():
                leftover_amount = ceil(amount) - amount
                leftovers.append((ingredient, leftover_amount, unit))
        return leftovers


if __name__ == '__main__':
    hummus_classic = Recipe(
        name='Hummus',
        ingredients=[Ingredient.knoblauchzehe, Ingredient.kichererbsen],
        amounts=[2.0, 1.0],
        units=[Unit.stueck, Unit.dose]
    )
    print(hummus_classic)
    print(hummus_classic.leftovers())
