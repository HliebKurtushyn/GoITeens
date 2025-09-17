# 1
# class StringIterator:
#     def __init__(self, string):
#         self.string = string
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.string):
#             character = self.string[self.index]
#             self.index += 1
#             return character
#         raise StopIteration
#
# for char in StringIterator('Hello'):
#     print(char)

# 2
# class StepIterator:
#     def __init__(self, numbers, step):
#         self.numbers = numbers
#         self.step = step
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.numbers):
#             num = self.numbers[self.index]
#             self.index += self.step
#             return num
#         raise StopIteration
#
# for item in StepIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1):
#     print(item)

#------------------------------------------------------
# ---HOMEWORK---
#------------------------------------------------------
# 1
# class Generate:
#     def __init__(self, start):
#         self.current = start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         value = self.current
#         self.current += 1
#         return value
#
# class Filter:
#     def __init__(self, iterable):
#         self.iterable = iterable
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while True:
#             value = next(self.iterable)
#             if value % 2 == 0:
#                 return value
#
# class Square:
#     def __init__(self, iterable):
#         self.iterable = iterable
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         value = next(self.iterable)
#         return value ** 2
#
# generated_nums = Generate(0)
# even_filtered_nums = Filter(generated_nums)
# squared_nums = Square(even_filtered_nums)
#
# result = [next(squared_nums) for i in range(10)]
# print(result)

# 2
class FlatIterator:
    def __init__(self, nested_list):
        self.stack = [iter(nested_list)]

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            current_iter = self.stack[-1]
            next_item = next(current_iter, None)

            if next_item is None:
                self.stack.pop()
                continue

            if isinstance(next_item, list):
                self.stack.append(iter(next_item))
            else:
                return next_item

        raise StopIteration

nested_list = [1, [2, [3, 4], 5], [6, 7], 8, [9 , 10, ['Test']]]
flat_iterator = FlatIterator(nested_list)

print(list(flat_iterator))

#---
# В додаткових завданнях я не зміг зрозуміти сам сенс задач. Саму тему я зрозумів на 50/50 але задачі для мене виглядають заплутано((
#---