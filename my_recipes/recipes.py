from src.ingredient import Ingredient
from src.item import Item
from src.recipe import Recipe
from src.unit import Unit


hummus_paprika = Recipe(
    name='Hummus',
    items=[
        Item(Ingredient.knoblauchzehe, 2.0, Unit.stueck),
        Item(Ingredient.kichererbsen, 1.0, Unit.dose),
        Item(Ingredient.gegrillte_paprika, 0.25, Unit.glas)
    ]
)