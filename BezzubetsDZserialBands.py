# # Есть некоторый словарь, который хранит названия
# # музыкальных групп(исполнителей) и альбомов. Название группы используется в качестве ключа, название
# # альбомов в качестве значения. Необходимо реализовать:
# # добавление данных, удаление данных, поиск данных,
# # редактирование данных, сохранение и загрузку данных
# # (используя упаковку и распаковку).
# import json
#
# bands = {
#         'The Beatles': 'White album',
#         'Michael Jakson': 'Thriller',
#         'Led Zeppelin': 'Led Zeppelin|||',
#         'Pind Floyd': 'The Wall'
# }
# print('\n', bands)  # Check this dictionary
# bands['Michael Jakson'] = 'Dangerous'
# print('\n', bands)  # Write another album)))
# bands['Led Zeppelin'] = 'Led Zeppelin |V'
# print('\n', bands)  # Write a right number))))
# del bands['Michael Jakson']
# print('\n', bands)  # Delete MJ. He is not a band))))
# for key in bands.keys():  # Just keys
#     print(key)
# for value in bands.values():  # Just values
#     print(value)
#
# # Packing
# with open("bands.json", "w") as write_file:
#     json.dump(bands, write_file)
#
# # Unpacking
# with open("bands.json", "rb") as f:
#     data_new = json.load(f)
#     print(data_new)