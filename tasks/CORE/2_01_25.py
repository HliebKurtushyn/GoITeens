# 1
# inp = input('Введіть рядок: ').lower()
# banned_words = ['ad', 'ads', 'adverting', 'spam', 'buy', 'sale', 'proposition', 'shop']
#
# for banned in banned_words:
#     if inp.find(banned) != -1:
#         print('This message may be a spam')
#         break

# 2
# text = 'Добрий день, еверібаді. А зараз музиченьки, як навалимо.'
# print(text.split())

# 3
delimiter = '-' * 80
total = 0

products = {
    'orange': [1, 'Апельсин', 6, 150],
    'lemon': [2, 'Лимон', 8, 90],
    'potato': [3, 'Картопля', 123, 445]
}

print(delimiter)
print("|{:^5}|{:<45}|{:>15}|{:>10}|".format('№', 'Товар', 'Кількість', 'Ціна'))
print(delimiter)
for product in products.values():
    print("|{:^5}|{:<45}|{:>15}|{:>10}|".format(product[0], product[1], product[2], product[3]))
    total += product[3]
print(delimiter)
print("|{:<67}|{:>10}|".format('Загальна вартість', total))
print(delimiter)

