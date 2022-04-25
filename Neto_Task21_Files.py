File_Name = 'recipes.txt'


def get_recipes_dict(file_name: str):
    """Form a dictionary of dishes with ingredients."""
    with open(file_name, encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            if '|' not in line and not line.strip().isdigit() and line.strip():
                dish = line.strip()
                cook_book[dish] = []
            elif '|' in line:
                cook_book[dish].append({'ingredient_name': line.split(' | ')[0],
                                        'quantity': int(line.split(' | ')[1]),
                                        'measure': line.split(' | ')[2].strip()})
        return cook_book


def get_shop_list_by_dishes(dishes: list, person_count: int):
    """Form a dict of ingredients taking into account the selected dishes and the number of persons."""
    shop_list = {}
    cook_book = get_recipes_dict(File_Name)
    for dish, ingredients in cook_book.items():
        if dish in dishes:
            for ingredient in ingredients:
                if ingredient['ingredient_name'] in shop_list:
                    quantity_in_shop_list = shop_list.get(ingredient['ingredient_name']).get('quantity')
                    shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                                'quantity': ingredient['quantity'] *
                                                                            person_count + quantity_in_shop_list}
                else:
                    shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                                'quantity': ingredient['quantity'] * person_count}
    return shop_list


print(get_recipes_dict(File_Name))
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2))
