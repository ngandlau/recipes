from src.ingredient import Ingredient
from src.recipe import Recipe
from src.find_recipes import find_recipe_given_leftovers
from src.unit import Unit

def test_find_recipe_given_leftovers():
    recipe = Recipe(
        name='hummus',
        ingredients=[Ingredient.kichererbsen, Ingredient.gegrillte_paprika],
        amounts=[0.5, 0.25],
        units=[Unit.dose, Unit.glas]
    )

    recipe_with_1_common_ingredients = Recipe(
        name='',
        ingredients=[Ingredient.kichererbsen],
        amounts=[1.0],
        units=[Unit.dose]
    )

    recipe_with_2_common_ingredients = Recipe(
        name='',
        ingredients=[
            Ingredient.nudeln,
            Ingredient.kichererbsen,
            Ingredient.gegrillte_paprika
        ],
        amounts=[
            250.0,
            1.0,
            0.5
        ],
        units=[
            Unit.gramm,
            Unit.dose,
            Unit.glas
        ]
    )

    recipe_with_0_common_ingredients = Recipe(
        name='',
        ingredients=[Ingredient.moehre],
        amounts=[5.0],
        units=[Unit.stueck]
    )

    recipes = [
        recipe,
        recipe_with_2_common_ingredients,
        recipe_with_1_common_ingredients,
        recipe_with_0_common_ingredients,
    ]
    
    soll = [
        (recipe_with_2_common_ingredients, 2),
        (recipe_with_1_common_ingredients, 1)
    ]
    ist = find_recipe_given_leftovers(recipe, recipes)
    assert ist == soll

