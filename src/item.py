from dataclasses import dataclass
from src.ingredient import Ingredient
from src.unit import Unit

@dataclass
class Item:
    ingredient: Ingredient
    amount: float
    unit: Unit

