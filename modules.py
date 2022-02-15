import pandas as pd
from functools import partial

def find_recipes(x, user_ingredients):
    return len(user_ingredients.intersection(x))


def linker(selected_recipe, dataframe):
    recipe_ingredients = dataframe.loc[dataframe['recipe_id'] == selected_recipe]
    to_get_url = recipe_ingredients.loc[recipe_ingredients.index[0]]
    return 'https://eda.ru/recepty/' + to_get_url['type'] + '/' + to_get_url['name']


def search_by_ingredients(my_ingredients, dataframe):
    links = []
    by_recipes = dataframe.groupby('recipe_id').agg({'ingredient': set})
    searching = partial(find_recipes, user_ingredients=my_ingredients)
    result = by_recipes['ingredient'].apply(searching)

    selected_recipes = list(result.sort_values(axis=0, ascending=False)[:5].index)
    for recipe in selected_recipes:
        links.append(linker(recipe, dataframe))

    return links
