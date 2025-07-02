# Задание 1 (List)
# numbers = [10, 25, 30, 40, 50, 60]
# element_in_list = int(input("Какой элемент коллекции вывести на экран? "))
# print(numbers[element_in_list])
# number_to_replacement = int(input("На какое число его заменить? "))
# numbers.insert(element_in_list, number_to_replacement)
# numbers.extend([number_to_replacement])
# print(numbers)

# Задание 2 (Кортеж или Tuple)
# colors = ('красный', 'зеленый', 'синий')
# element_in_tuple = int(input("Какой элемент кортежа вывести на экран? "))
# print(colors[element_in_tuple])
# color_to_replacement = input("На какой цвет его заменить? ")
# list_to_replace = list(colors)
# list_to_replace.insert(element_in_tuple, color_to_replacement)
# colors_2 = tuple(list_to_replace)
# colors_3 = (colors + (color_to_replacement,))
# print(colors)
# print(colors_2)
# print(colors_3)

# Задание 3 (Set)
# set_1 = {1, 2, 3, 4, 5}
# set_2 = {4, 5, 6}
# general_elements = set_1 & set_2
# print(general_elements)
# set_1.update(set_2)
# print(set_1)
# element_to_remove = int(input("Какое значение из второго множества удалить? "))
# set_2.remove(element_to_remove)
# print(set_2)

# Задание 4 (Словарь)
person = {
    "name": "Сергей",
    "surname": "Собянин",
    "city": "Москва"
}
print(person["name"])
person["age"] = 50
del person["surname"]
print(person)

