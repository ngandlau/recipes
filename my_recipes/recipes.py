from src.ingredient import Ingredient
from src.recipe import Recipe
from src.unit import Unit


hummus_paprika = Recipe(
    name='Hummus',
    ingredients=[
        Ingredient.knoblauchzehe,
        Ingredient.kichererbsen,
        Ingredient.gegrillte_paprika
    ],
    amounts=[
        2.0, 
        1.0,
        0.25
    ],
    units=[
        Unit.stueck,
        Unit.dose,
        Unit.glas
    ]
)

onepot_nudel = Recipe(
    name='Onepot Nudeln mit cremiger Hummus-Sauce',
    ingredients=[
        Ingredient.nudeln,
        Ingredient.hummus_classic,
        Ingredient.gegrillte_paprika
    ],
    amounts=[
        250.0,
        100.0,
        0.5
    ],
    units=[
        Unit.gramm,
        Unit.gramm,
        Unit.glas
    ]
)

quiche_veggie = Recipe(
    name='Vegetarischer Quiche mit Zucchini-Möhren-Füllung',
    ingredients=[
        Ingredient.quiche_teig,
        Ingredient.zwiebel_weiss,
        Ingredient.zucchini,
        Ingredient.moehre
    ],
    amounts=[
        1.0,
        1.0,
        1.0,
        3.0
    ],
    units=[
        Unit.stueck,
        Unit.stueck,
        Unit.stueck,
        Unit.stueck
    ]
)
