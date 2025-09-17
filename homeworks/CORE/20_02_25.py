# 1
# def sum_to_n(n):
#     if n == 1:
#         return 1
#     return n + sum_to_n(n - 1)
#
# print(sum_to_n(10))

# 2
# def recursive_reversed(text):
#     if len(text) == 0:
#         return text
#     return recursive_reversed(text[1:]) + text[0]
#
# print(recursive_reversed("Hello World!"))

# 3
# def count_symbol(text, symbol):
#     if len(text) == 0:
#         return 0
#     return (1 if text[0] == symbol else 0) + count_symbol(text[1:], symbol)
#
# print(count_symbol("xdhxasx", "x"))