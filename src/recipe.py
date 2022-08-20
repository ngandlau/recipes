from dataclasses import dataclass
from math import ceil
from typing import List, Tuple
from src.item import Item

from src.unit import Unit
from src.ingredient import Ingredient

@dataclass
class Recipe:
    name: str
    items: List[Item]

    def get_ingredients(self) -> List[Ingredient]:
        return [item.ingredient for item in self.items]

    def get_leftovers(self) -> List[Item]:
        leftovers = []
        for item in self.items:
            if not item.amount.is_integer():
                leftover_amount = ceil(item.amount) - item.amount
                leftovers.append((item.ingredient, leftover_amount, item.unit))
        return leftovers