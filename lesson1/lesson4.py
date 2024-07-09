"""
    ТЕМА: Структуры данных
    list, tuple, set, dict
"""

"""list []"""
# my_list = ["Рамзан", "Жаркынай", "Чынгыз", "Нуркамил", "Самат"]
# print(my_list)

"""Index"""
# print(my_list[2])
# print(my_list[4])

"""Add"""
# my_list.append("Asan")
# my_list.extend(["Batma", "Aygul", "Bakyt"])
# my_list.insert(0, "Talant")
# print(my_list)

"""Edit"""
# my_list[0] = "Islam"
# my_list.sort()
# my_list.reverse()
# print(my_list)

"""Delete"""
# my_list.remove("Чынгыз")
# my_list.pop(3)
# del my_list[1]
# print(my_list)


# print(my_list.index("Самат"))
# print(my_list.count("Самат"))

"""Cрезы [start:stop:step]"""
# print(my_list[:3])
# print(my_list[1:])

"""Tuple ()"""
# my_tuple = "Рамзан", "Жаркынай", "Жаркынай", "Чынгыз", "Нуркамил", "Самат"
# print(my_tuple)
# print(my_tuple.count("Жаркынай"))
# print(my_tuple.index("Чынгыз"))
# print(my_tuple[0])
# my_number = 5
# print(type(my_number))
# my_number2 = 5,
# print(type(my_number2))


"""Set {}"""
# my_number = {1, 1, 2, 3, 4, 4, 5, 5, 5, 6}
# print(my_number)

"""Dict {}"""
my_dict = {
    "name": "Asan",
    "surname": "Asanov",
    "age": 14
}

# print(my_dict['name'])

# my_dict['name'] = "Bakyt"
# my_dict['hobby'] = "Running"
# print(my_dict)

# my_dict.pop('name')
# print(my_dict)

print(my_dict.items())