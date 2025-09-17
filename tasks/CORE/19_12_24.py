# 1
# first_list = list()
# second_list = list()
#
# add_element = None
#
# while add_element != "stop":
#     try:
#         add_element = int(input("Введіть число для додавання: (stop щоб зупинитись)"))
#     except:
#         break
#     first_list.append(add_element)
#
# for element in first_list:
#     if element % 2 == 0:
#         second_list.append(element)
#
# print(f"{first_list}\n{second_list}")

# 2
# to_do = list()
# add_todo = None
# while add_todo != "q":
#     add_todo = input("Додати завдання (q - вихід)")
#     to_do.append(add_todo)
# to_do.remove("q")
#
# for element in to_do:
#     print(f"-{element}")

# 3
# to_do = list()
# add_todo = None
# choice = None
# while add_todo != "q":
#     add_todo = input("Додати завдання (q - стоп)")
#     to_do.append(add_todo)
# to_do.remove("q")
# add_todo = None
#
# for element in to_do:
#     print(f"-{element}")
#
# while choice != "q":
#     choice = input("Введіть дію\n1 - Видалити елемент списку\n2 - Сортування списку у зворотньому порядку (q - вийти з програми)")
#
#     if choice == "1":
#         while add_todo != "q":
#             add_todo = input("Введіть елемент який ви хочете видалити (q - стоп)")
#             try:
#                 to_do.remove(add_todo)
#             except:
#                 print("Такого елемента немає в списку!")
#     elif choice == "2":
#         to_do = sorted(to_do, reverse=True)
#         print("Готово!")
#
# for element in to_do:
#     print(f"-{element}")