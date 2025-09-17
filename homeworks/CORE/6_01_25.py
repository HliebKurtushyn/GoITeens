# 1
# string = input("Введіть рядок: ")
#
# for letter in string:
#     if letter.isdigit():
#         string = string.replace(letter, '')
#
# print(string)

# 2
# surname = input("Введіть прізвище: ").lower()
# letter_count = {}
#
# for letter in surname:
#     if letter in letter_count:
#         letter_count[letter] += 1
#     else:
#         letter_count[letter] = 1
# most_frequent_letter = max(letter_count, key=letter_count.get)
# print(f"Найчастіше зустрічається буква '{most_frequent_letter}' у вашому прізвищі")
