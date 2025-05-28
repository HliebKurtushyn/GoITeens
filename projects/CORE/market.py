all_products = ['Apple', 'Banana', 'Pineapple', 'Milk', 'Juice']
sales_history = []


def add_product():
    while True:
        add_new = input("Введіть який продукт ви хочете додати:  (S - стоп)")

        if add_new == "S":
            break
        elif add_new not in all_products:
            all_products.append(add_new)
            print(f"Новий список: {all_products}")

        else:
            print("Введене не коректне значення або продукт вже існує!")


def replace_product():
    while True:
        replace = input("Введіть продукт який ви хочете замінити:  (S - стоп)")

        if replace in all_products:
            while True:
                insert = input("Введіть назву продукту який ви хочете додати: (S - стоп)")

                if insert == "S":
                    break
                elif insert not in all_products:
                    replace_index = all_products.index(replace)

                    all_products.remove(replace)
                    sales_history.append(replace)

                    all_products.insert(replace_index, insert)
                    print(f"Новий список: {all_products}")

                else:
                    print("Введене не коректне значення або продукту немає в списку!")
        elif replace == "S":
            break

        else:
            print("Введене не коректне значення або продукту немає в списку!")


def delete_product():
    while True:
        delete = input("Введіть продукт який ви хочете позначити як проданий або ж видалити: (S - стоп)")

        if delete == "S":
            break
        elif delete in all_products:
            all_products.remove(delete)
            sales_history.append(delete)
            print(f"Новий список: {all_products}")
        elif delete == "S":
            break

        else:
            print("Введене не коректне значення або продукту немає в списку!")


print("------------------------------------------------------")
print("------------------------------------------------------")
print("Вітаємо, адмін!")
print("------------------------------------------------------")
print("------------------------------------------------------\n\n")

while True:
    choice = input(
        "Що ви бажаєте зробити?\n1 - перевірити список продуктів в наявності\n2 - додати продукт\n3 - "
        "видалити/позначити проданим продукт\n4 - замінити наявний продукт новим\n5 - перевірити історію продажів\n6 "
        "- вихід\n")

    if choice == "1":
        print(all_products)
    elif choice == "2":
        add_product()
    elif choice == "3":
        delete_product()
    elif choice == "4":
        replace_product()
    elif choice == "5":
        print(sales_history)
    elif choice == "6":
        break
        