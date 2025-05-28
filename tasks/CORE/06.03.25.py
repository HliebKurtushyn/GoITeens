from random import randint

# 1
# def check_and_sort(nums):
#     only_positive = [num for num in nums if num > 0]
#     return f"Are all numbers positive: {all(num > 0 for num in nums)}\nSorted numbers: {sorted(only_positive)}"
#
# print(check_and_sort([randint(-20, 100), randint(-20, 100), randint(-20, 100), randint(-20, 100), randint(-20, 100)]))
#
# 2
# vowels = ['а', 'е', 'є', 'и', 'і', 'ї', 'о', 'у', 'ю', 'я', 'a', 'e', 'i', 'o', 'u']
#
# def check_vowels(user_input: list[str]):
#     return f"Чи має рядок голосні: {any(letter in word for word in user_input for letter in vowels)}"
#
# user_input = input("Введіть рядок: ").lower().split()
# print(check_vowels(user_input))

# 3
def sort_data(data):
    sorted_data = sorted(data, key=lambda person: person['age'], reverse=True)

    new_sorted_data = ''.join(f"{person['name']}: {person['age']}\n" for person in sorted_data)
    original_data = ''.join(f"{person['name']}: {person['age']}\n" for person in data)

    return f"Original data:\n{original_data}\n\nSorted data:\n{new_sorted_data}"

personal_data = [
    {'name': 'Gleb', 'age': 13},
    {'name': 'Oleh', 'age': 9},
    {'name': 'Sasha', 'age': 16},
    {'name': 'Denis', 'age': 18}
]
print(sort_data(personal_data))