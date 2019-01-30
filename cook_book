cook_book = {}

with open('./recipes.txt', encoding="utf-8") as file:
    for k, line in enumerate(file):
        ingredients_list = []
        if k > 0:
            dish = file.readline().strip()
        else:
            dish = line.strip()
        ingredients_len = int(file.readline().strip())
        while ingredients_len > 0:
            ingredient = {}
            ingredient_list = file.readline().strip().split('|')
            ingredient['ingredient_name'] = ingredient_list[0].strip()
            ingredient['quantity'] = ingredient_list[1].strip()
            ingredient['measure'] = ingredient_list[2].strip()
            ingredients_len -= 1
            ingredients_list.append(ingredient)
        cook_book[dish] = ingredients_list

print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    ingredients_dict = {}
    for item in dishes:
        dish_ingredients = cook_book[item]
        for dish_ingredient in dish_ingredients:
            name = dish_ingredient['ingredient_name']
            measure = dish_ingredient['measure']
            quantity = int(dish_ingredient['quantity'])
            quantity_by_person = quantity * person_count
            if not ingredients_dict.get(name):
                ingredients_dict[name] = {'measure': measure, 'quantity': quantity_by_person}
            else:
                old_quantity = ingredients_dict[name]['quantity']
                ingredients_dict[name]['quantity'] = old_quantity + quantity_by_person

    return ingredients_dict


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

