# 1
# def summa(x: int, y: int) -> int:
#     return x + y
#
# print(summa(5, 5))

# 2
# ---------------
# Не зрозумів завдання
# ---------------

# 3
# def logging_outer(func):
#     def logging_inner(*args, **kwargs):
#         print(f"[INFO] Аргументи {args}, {kwargs} були викликані з функцією {func.__name__}")
#         result = func(*args, **kwargs)
#         print(f"Результат функції {func.__name__}:")
#         print(result)
#         return result
#     return logging_inner
#
#
# @logging_outer
# def some_func(x, y):
#     return x + y
#
# some_func(3, 5)

# 4
# def counter():
#     count = 0
#
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             nonlocal count
#             count += 1
#             print(f"Функція {func.__name__} була викликана {count} разів")
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator
#
# @counter()
# def some_func(x, y):
#     return x + y
#
# @counter()
# def another_func():
#     return "Hello"
#
# print(some_func(5, 5))
# print(another_func())
# print(some_func(3, 13))

# 5
# import time
#
# def timer(func):
#     def wrapper(*args, **kwargs):
#         print(f"Старт функції {func.__name__}")
#
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#
#         print(f"Кінець функції {func.__name__}.\nВона виконувалась {end - start}")
#
#         return result
#
#     return wrapper
#
# @timer
# def test_func():
#     for _ in range(100000000):
#         pass
#
# print(test_func())

# 6
# ---------------
# Не зрозумів завдання
# ---------------

# 7
# def plus_one(nums_list: list[int]) -> list[int]:
#     new_list = []
#     for el in nums_list:
#         el += 1
#         new_list.append(el)
#
#     return new_list
#
# print(plus_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# 8
# def return_length(text: str) -> int:
#     return len(text)
#
# print(return_length("Hello World!"))