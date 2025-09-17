# 1
# def open_file(path):
#     try:
#         file = open(path, 'r')
#         content = file.read()
#         return content
#     except FileNotFoundError:
#         return 'File not found'
#     finally:
#         try:
#             file.close()
#             print('File closed')
#         except NameError:
#             return 'Name error'
#
#
# print(open_file('another_test.txt'))

# 2
# def division(num1, num2):
#     try:
#         return num1 / num2
#     except ZeroDivisionError:
#         return "Ділення на нуль!"
#     except TypeError:
#         return "Введіть число!"
#
# print(division(10, 2))
# print(division(10, 0))
# print(division('not num', 2))

# 3
# def get_element_by_index(my_list, index):
#     try:
#         element = my_list[index]
#         return element
#     except IndexError:
#         return 'Індекс вийшов за межі списку!'
#
# my_list = [1, 2, 3, 4, 5 , 6, 7, 8, 9]
# print(get_element_by_index(my_list, 6))
# print(get_element_by_index(my_list, 9))

# 4
# def user_division():
#     try:
#         num1 = int(input("Ведіть перше число: "))
#         num2 = int(input("Ведіть друге число: "))
#         return num1 / num2
#     except ValueError:
#         return 'Введіть число!'
#     except ZeroDivisionError:
#         return 'Ділення на нуль!'
#
# print(user_division())

# 5
# class LessThanEightLength(Exception):
#     ...
#
# class NoNumbers(Exception):
#     ...
#
# def check_password(password: str):
#     if not any(el.isdigit() for el in password):
#         raise NoNumbers('Пароль має містити хоча б одну цифру!')
#     if len(password) < 8:
#         raise LessThanEightLength('Пароль має бути довжиною хоча б 8 символів!')
#
# try:
#     password = 'fgd1fh'
#     check_password(password)
# except NoNumbers as e:
#     print(e)
# except LessThanEightLength as e:
#     print(e)
# else:
#     print('Пароль прийнятий')


























