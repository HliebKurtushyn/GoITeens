print("Введіть координати для")
x = int(input("X: "))
y = int(input("Y: "))

def coordinates():
    if x > 0 and y > 0:
        return "1 чверть"
    elif x < 0 and y > 0:
        return "2 чверть"
    elif x < 0 and y < 0:
        return "3 чверть"
    elif x > 0 and y < 0:
        return "4 чверть"
    else:
        "Точка знаходиться на осі"

print(coordinates())