# 1
# numbers = [int(i) for i in input().split()]
# suma = 0

# for number in numbers:
#     suma += number

# print(suma)

# 2
# colors = ['red', 'green', 'blue', 'yellow']

# for x in colors:
#     print(x)
# else:
#     print("\n-------------------------------------")
#     print("Done!")
#     print("-------------------------------------\n")

# 3
a = int(input())
b = int(input())

sum = 0
count = 0

for i in range(a, b + 1):
    if (i % 3) == 0:
        sum += i
        count += 1

print(sum / count)