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
}


def dish(request, name):
    servings = int(request.GET.get('servings', 1))
    name_of_dish = name
    after_servings = {}
    if servings > 1:
        for name_ingr, count_ingr in DATA[name_of_dish].items():
            after_servings[name_ingr] = count_ingr * servings
    elif name_of_dish not in DATA:
        after_servings = None
    else:
        after_servings = DATA[name_of_dish]
    context = {
        'recipe': after_servings
    }

    return render(request, 'calculator/index.html', context)