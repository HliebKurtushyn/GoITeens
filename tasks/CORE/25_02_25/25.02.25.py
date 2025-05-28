# 1
# with open('Task 1/input.txt', 'r') as file:
#     input_data = file.readlines()
#
# new_input_data = list(set(input_data))
#
# with open('Task 1/output.txt', 'w+') as file:
#     output_data = file.writelines(new_input_data)
#
# print(f"Output: {output_data}")

# 2
# def lines(path):
#     with open(path, 'r') as file:
#         return len(file.readlines())
#
# print(f"Кількість рядків в файлі: {lines('Task 1/input.txt')}")

# 3
# with open('Task 2/data.txt', 'r') as file:
#     print(len(file.read().split()))

# 4
# def count_word(path, word):
#     with open(path, 'r') as file:
#         content = file.read()
#         return content.count(word)
#
# print(count_word('Task 2/data.txt', 'Hello'))

# 5

# 6
# with open('Task 6/text.txt.py', 'r') as file:
#     content = file.read()
#
# if content == "":
#     print("File in empty!")
# else:
#     print("File is not empty!")