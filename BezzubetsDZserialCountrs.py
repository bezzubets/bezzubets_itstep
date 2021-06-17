# # Есть некоторый словарь, который хранит названия
# # стран и столиц. Название страны используется в качестве
# # ключа, название столицы в качестве значения. Необходимо
# # реализовать: добавление данных, удаление данных, поиск
# # данных, редактирование данных, сохранение и загрузку
# # данных (используя упаковку и распаковку).
# import json
# c1 = {
#         'Ukraine': 'Kyiv',
#         'USA': 'Washington',
#         'Turkey': 'Ankara',
#         'New Zealand': 'Wellington'
# }
# print('\n', c1)  # Check this dictionary
# c1['Turkey'] = 'Istanbul.no?)'
# print('\n', c1)  # Write wrong capital)))
# c1['USA'] = 'Los Angeles)))'
# print('\n', c1)  # Write second wrong capital))))
# del c1['USA']
# print('\n', c1)  # Delete USA. Not a country))))
# for key in c1.keys():  # Just keys
#     print(key)
# for value in c1.values():  # Just values
#     print(value)
# # Packing
# with open("c1.json", "w") as write_file:
#     json.dump(c1, write_file)
# # Unpacking
# with open("c1.json", "rb") as f:
#     data_new = json.load(f)
#     print(data_new)