# 1
# listok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_listok = [x for x in listok if x % 2 == 0]

# print(new_listok)

# 2
# listok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in range(0, len(listok), 2):
#     print(listok[i])

# 3
# listok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_listok = [x for x in listok if x % 2 != 0]

# print(new_listok)

# 4
# listok = ["apple", "juice", "milk"]
# listok.reverse()
# print(listok)

# 5
# listok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# middle_listok = sum(listok) / len(listok)
# lower_than_middle = [x for x in listok if x < middle_listok]

# print(lower_than_middle)

# 6
# listok = ["apple", "juice", "milk"]
# N = 4

# words = [x for x in listok if len(x) > N]
# print(words)

# 7
# l1 = ["He", "m", "ho", "i", "cod"]
# l2 = ["llo", "y", "bby", "s", "ing"]

# result = [a + b for a, b in zip(l1, l2)]
# print(result)

# 8
# listok = [1, 3, 4, 6, 8, 10]
# N = 10

# result = [x for x in range(1, N + 1) if x not in listok]
# print(result)

# 9
# listok = ["apple", "juice", "milk", "cake"]

# short = min(len(word) for word in listok)
# shortest = [word for word in listok if len(word) == short]

# print(shortest)


