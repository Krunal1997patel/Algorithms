#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    small = []

    if len(recipe) <= 0 or len(ingredients) <= 0 or len(recipe) < len(ingredients):
        return 0

    for iteam in recipe:
        if iteam not in ingredients:
            return 0
        else:
            small.append(ingredients[iteam] // recipe[iteam])
    return min(small)


print(
    recipe_batches(
        {"milk": 2, "sugar": 40, "butter": 20}, {"milk": 5, "sugar": 120, "butter": 500}
    )
)

if __name__ == "__main__":
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {"milk": 100, "butter": 50, "flour": 5}
    ingredients = {"milk": 132, "butter": 48, "flour": 51}
    print(
        "{batches} batches can be made from the available ingredients: {ingredients}.".format(
            batches=recipe_batches(recipe, ingredients), ingredients=ingredients
        )
    )

