# 1
# name = input("Ваше імя будь ласка: ")

# while len(name) < 1:
#     name = input("Ваше імя будь ласка: ")

# print(f"Ваше ім'я {name}")

# 2
# a = int(input("A: "))
# b = int(input("B: "))

# summa = 0

# for i in range(a, b + 1):
#     summa += i

# print(summa)

# 3
# number = int(input("Number: "))

# for i in range(1, 11):
#     result = number * i
#     print(f"{result} ")

# 4
# for num in range(-10, 0):
#     print(num)

# 5
# a = 1

# while a <= 15:
#     print(a)
#     a += 1

# 6
# names = ["Sasha", "Sashko", "Oleksandr", "Oleksandrik"]

# for hi in names:
#     print(f"Hello {hi} ")

# 7
# word = "Civilization"
# num = 0

# for letter in word:
#     if letter == "i":
#         num += 1
# print(f"У цьому слові {num} букви і")

# 8
# word = input("Введіть слово: ")
# input_letter = input("Введіть слово для пошуку: ")
# num = 0

# for letter in word:
#     if letter == input_letter:
#         num += 1
# print(f"У цьому слові {num} букви {letter}")

# 9
# name = "Oleksandr"

# for letter in name:
#     print(letter)

# else:
#     print("Завершено")

# 10
# n = int(input("Number: "))

# for i in range(1, n + 1):
#     cube = i ** 3
#     print(f"Cube of number {i} is {cube}")

# 11
# price = 10
# weight = 1

# for i in range(1, 11):
#     total_price = price * i
#     print(f"Вартість {i} кг цукерок: {total_price}")

# 12
# price_per_kg = float(input("Введіть ціну 1 кг цукерок: "))

# weight = 1.2
# while weight <= 2:
#     total_price = price_per_kg * weight
#     print(f"Вартість {weight} кг цукерок: {total_price:.2f} грн")
#     weight += 0.2

# 13
# for num in range(0, 101):
#     if num % 2 == 0:
#         print(num)

# 14
# start = int(input("Введіть початкове значення діапазону: "))
# end = int(input("Введіть кінцеве значення діапазону: "))

# for num in range(start, end + 1):
#     if num % 2 != 0:
#         print(num)

# print(0)

# 15
# n = int(input("Введіть число для обчислення факторіалу: "))

# factorial = 1

# if n < 0:
#     print("Факторіал для від'ємного числа не існує.")
# else:
#     while n > 1:
#         factorial *= n
#         n -= 1

#     print(f"Факторіал числа: {factorial}")

# 16
# a = int(input("число a: "))
# b = int(input("число b: "))
# c = int(input("число c: "))

# count = 0

# for num in range(a, b + 1):
#     if num % c == 0:
#         count += 1

# print(f"Кількість чисел між {a} і {b} які діляться на {c}: {count}")
