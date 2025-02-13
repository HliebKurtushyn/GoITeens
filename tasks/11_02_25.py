# 1
# owners = {"AI3468AA": "Gleb Kurtushyn",
#           "AA6843UE": "Sasha Dolenko",
#           "AH4387TR": "Gleb Kurtushyn",
#           "AK4632BU": "Denis Skipin",
#           "AB5621NU": "Matvii Ivanov"}
#
# find_auto = "AI3468AA"
# car_owner = owners.get(find_auto, None)
# print(f"{car_owner} is owner of auto with number plate {find_auto}")
#
# car_owners = dict()
# for owner in owners.values():
#     if car_owners.get(owner, 0) == 0:
#         car_owners[owner] = 1
#     else:
#         auto_count = car_owners[owner]
#         auto_count += 1
#         car_owners[owner] = auto_count
#
# for pip, auto_count in car_owners.items():
#     if auto_count > 1 :
#         print('Власник {} має наступну кількість авто - {}'.format(pip, auto_count))
from itertools import count

# 2
# stock = {
#     "Apple": 15,
#     "Banana": 5,
#     "Apple juice": 2
# }
#
# to_buy = input("Enter what you would like to buy separated by space: ").split()
#
# if to_buy[0] in stock:
#     if int(to_buy[1]) > stock[to_buy[0]]:
#         print("Not enough in stock")
#     else:
#         stock[to_buy[0]] -= int(to_buy[1])
#         print("ok")
# else:
#     print("Theres no such product in the stock")

# 3
# users = {
#     "Gleb": [13, "male", 'gleb_kurt@example.com'],
#     "Sasha": [14, "male", "sasha_dol@example.com"]
# }
#
# info = input("Enter username to get info separated by space: ").split()
#
# for user in info:
#     print(f"Age: {users[user][0]}\nGender: {users[user][1]}\nE-mail: {users[user][2]}\n")

# 4
# students = {
#     "Gleb": [1, 3, 6, 6, 4, 2, 3],
#     "Sasha": [6, 6, 6, 5, 4, 6]
# }
#
# info = input("Enter name of student you want to know average grade: ").strip()
#
# if info in students:
#     grades = students[info]
#     average_grade = sum(grades) / len(grades)
#     print(f"{info}'s average grade is: {average_grade:.2f}")
# else:
#     print("Theres no such student.")



















