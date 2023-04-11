from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)

    'vodka': {
        'водка, мл': 250,
        'сало, г': 100,
        'хлеб, ломтик': 5
    }

}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def recipe_calc(request, recipe_name):
    persons = int(request.GET.get('servings', 1))
    context = {
        'name': recipe_name,
        'recipe': {ing: (amount * persons) for ing, amount in DATA[recipe_name].items()},
        'persons': persons
    }

    return render(request, 'calculator/index.html', context)
