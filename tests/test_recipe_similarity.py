from src.ingredient import Ingredient
from src.item import Item
from src.recipe import Recipe
from src.find_recipes import find_recipe_given_leftovers
from src.unit import Unit

def test_find_recipe_given_leftovers():
    leftovers = [
        Item(Ingredient.kichererbsen, 0.5, Unit.dose),
        Item(Ingredient.gegrillte_paprika, 0.25, Unit.glas),
    ]

    recipe_with_0_common_ingredients = Recipe(
        name='',
        items=[Item(Ingredient.moehre, 5.0, Unit.stueck)]
    )

    recipe_with_1_common_ingredients = Recipe(
        name='some',
        items=[
            Item(Ingredient.kichererbsen, 1.0, Unit.dose),
        ]
    )

    recipe_with_2_common_ingredients = Recipe(
        name='',
        items=[
            Item(Ingredient.nudeln, 250.0, Unit.gramm),
            Item(Ingredient.kichererbsen, 1.0, Unit.dose),
            Item(Ingredient.gegrillte_paprika, 0.5, Unit.glas)
        ]
    )


    recipes = [
        recipe_with_2_common_ingredients,
        recipe_with_1_common_ingredients,
        recipe_with_0_common_ingredients,
    ]
    
    soll = [
        (recipe_with_2_common_ingredients, 2),
        (recipe_with_1_common_ingredients, 1)
    ]
    ist = find_recipe_given_leftovers(leftovers, recipes)
    assert ist == soll

