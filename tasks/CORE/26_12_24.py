# 1
# a = input("First str: ")
# b = input("Second str: ")
#
# a_len = len(a)
# b_len = len(b)
#
# result = ''
#
# for string_1 in range(a_len):
#     for string_2 in range(string_1 + 1, a_len + 1):
#         if a[string_1:string_2] in b and len(a[string_1:string_2]) > len(result):
#             result = a[string_1:string_2]
#
# print(f"Найбільший загальний під рядок: {result}")

# 2
a = input("First str: ")
b = input("Second str: ")

a_len = len(a)
b_len = len(b)

result = ''

for string_1 in range(a_len):
    for string_2 in range(string_1 + 1, a_len + 1):
        if a[string_1:string_2] in b and len(a[string_1:string_2]) > len(result):
            result = a[string_1:string_2]


result_min = min(result)
print(f"Найбільший загальний під рядок: {result_min}")
