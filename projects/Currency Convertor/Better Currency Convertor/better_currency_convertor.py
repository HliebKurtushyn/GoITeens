import json
import os
from random import choice


# ---JSON---

def dump_to_json(type, obj):
    with open(f"Data files/{type}.json", "w") as file:
        json.dump(obj, file, indent=3)


def load_from_json(type):
    with open(f"Data files/{type}.json", "r") as file:
        return json.load(file)


# ---JSON---


# ---MAIN FUNCTIONS---

def clear_console():
    if os.name == 'nt':
        os.system('cls')


def check_length(element, max_length):
    if max_length is not None:
        return False if len(str(element)) > max_length else True


def convert(currencies, count=1.0):
    print(f"{count} UAH in other currencies:")
    for currency, rates in currencies.items():
        buy_rate = rates["buy"]
        sell_rate = rates["sell"]
        print(f"    {currency}:    BUY: {count / buy_rate:.2f} | SELL: {count / sell_rate:.2f}")


def convert_your_wallet(wallets, selected_wallet, user, currencies):
    if user in wallets and selected_wallet in wallets[user]:
        balance = wallets[user][selected_wallet].get("UAH", 0)
        print(f"Your converted wallet ({selected_wallet}):")
        print(f"  UAH: {balance}")

        for currency, rates in currencies.items():
            buy_rate = rates["buy"]
            print(f"    {currency}: {balance / buy_rate:.2f}")

    else:
        print(f"ERROR: Wallet '{selected_wallet}' not found for user '{user}'.")


# def add_new_wallet(name="New Wallet"):
#     if user in wallets:
#         wallets[user][name] = {}
#         return "Wallet has been successfully added" if name in wallets[user] else "Something went wrong"
#     else:
#         return "ERROR: User {user} not found"


def deposit(wallets, selected_wallet, user, json_data, json_passwords):
    if user in wallets and selected_wallet in wallets[user]:
        while True:
            dep_currency = input("Enter amount which you want to deposit (MAX '100.000 UAH'):\n   ")

            try:
                dep_currency = float(dep_currency)
            except ValueError:
                print("ERROR: Please, enter a valid number!")
                continue

            while True:
                pin = input("Your pin code:")
                if pin == json_passwords[user]["Pin code"]:
                    break
                else:
                    print("Invalid pin code!")

            if 0.0 < dep_currency <= 100000.0:
                wallets[user][selected_wallet]["UAH"] += dep_currency
                json_data['Wallets'] = wallets

                dump_to_json("data", json_data)

                print(f"{dep_currency:.2f} successfully added to {user}'s {selected_wallet}")
                break
            else:
                print("ERROR: Number must be between 0 and 100.000 UAH!")
    else:
        print("ERROR: User or wallet is not found")


def withdraw(wallets, selected_wallet, user, json_data, json_passwords):
    if user in wallets and selected_wallet in wallets[user]:
        while True:
            withdraw_currency = input("Enter amount which you want to withdraw (MAX '100.000 UAH'):\n   ")

            try:
                withdraw_currency = float(withdraw_currency)
            except ValueError:
                print("ERROR: Please, enter a valid number!")
                continue

            while True:
                pin = input("Your pin code: ")
                if pin == json_passwords[user]["Pin code"]:
                    break
                else:
                    print("Invalid pin code!")

            if wallets[user][selected_wallet].get("UAH", 0) < withdraw_currency:
                print("ERROR: Not enough money on your balance!")
                continue

            if 0.0 < withdraw_currency <= 100000.0:
                wallets[user][selected_wallet]["UAH"] -= withdraw_currency
                json_data['Wallets'] = wallets

                dump_to_json("data", json_data)

                print(f"{withdraw_currency:.2f} successfully withdrawn from {user}'s {selected_wallet}")
                break
            else:
                print("ERROR: Number must be between 0 and 100.000 UAH!")
    else:
        print("ERROR: User or wallet is not found")


def sign_up(wallets, json_passwords, json_cfg, json_data):
    while True:
        username = input("  Enter username: ")
        password = input("  Enter password: ")

        if username not in wallets:
            while True:
                pin = input("  Enter your new pin code: ")
                if check_length(pin, 4):
                    break
                else:
                    print("ERROR: Pin code must be maximum 4 numbers!")

            wallets[username] = {}
            json_passwords[username] = {}
            json_cfg[username] = {}

            wallets[username] = {"New Wallet": {"UAH": 0}, }
            json_passwords[username]['Password'] = password
            json_passwords[username]['Pin code'] = pin
            json_cfg[username]["selected_wallet"] = ""

            json_data["Wallets"] = wallets

            dump_to_json("data", json_data)
            dump_to_json("passwords", json_passwords)
            dump_to_json("cfg", json_cfg)

            print(f"Successfully signed up as {username}")

            start_screen(wallets, json_cfg, json_passwords, json_data)
            break

        else:
            print("ERROR: Username is already exists!")


def log_in(wallets, json_cfg, json_password):
    while True:
        username = input("  Enter username: ")
        password = input("  Enter password: ")

        if username in wallets and json_password[username]['Password'] == password:
            print(f"Successfully logged in as {username}!")
            json_cfg["logged_user"] = username
            dump_to_json("cfg", json_cfg)
            return username, True
        else:
            print("ERROR: Invalid username or password!")


def start_screen(wallets, json_cfg, json_passwords, json_data):
    choice = None
    print("Welcome in the BankApp!")

    print("1. Sign up")
    print("2. Log in")
    choice = input(": ")

    if choice == "1":
        sign_up(wallets, json_passwords, json_cfg, json_data)
    elif choice == "2":
        user, logged = log_in(wallets, json_cfg, json_passwords)


def log_out(wallets, user, json_cfg):
    user = None
    json_cfg["logged_user"] = None
    dump_to_json("cfg", json_cfg)


def choices(wallets, user, currencies, selected_wallet, json_cfg, logged, json_data, json_passwords):
    while logged:
        print("\nChoose an action:")
        print("1. Select wallet")
        print("2. Convert UAH")
        print("3. Convert your wallet balance")
        print("4. Deposit money")
        print("5. Withdraw money")
        print("6. Log out")
        print("7. Exit")

        choice = input(": ")

        if choice == "1":
            while True:
                print(f"Your wallets: {', '.join([w for w in wallets[user]])}")
                selected_wallet = input("Please, select one of your wallets: ")
                if selected_wallet in wallets[user]:
                    print(f"Wallet {selected_wallet} selected!")
                    break
                else:
                    print("ERROR: Invalid wallet! Try again.")

        elif choice == "2":
            amount = input("Enter amount in UAH to convert: ")
            try:
                amount = float(amount)
                convert(currencies, amount)
            except ValueError:
                print("ERROR: Please enter a valid number!")

        elif choice == "3":
            convert_your_wallet(wallets, selected_wallet, user, currencies)

        elif choice == "4":
            deposit(wallets, selected_wallet, user, json_data, json_passwords)

        elif choice == "5":
            withdraw(wallets, selected_wallet, user, json_data, json_passwords)

        elif choice == "6":
            log_out(wallets, user, json_cfg)
            logged = False
            print("Logging out...")

        elif choice == "7":
            print("Exit...")
            logged = False

        else:
            print("ERROR: Invalid choice! Try again.")


# ---APP FUNCTION---
def main():
    while True:
        json_data = load_from_json("data")
        json_cfg = load_from_json("cfg")
        json_passwords = load_from_json("passwords")

        user = json_cfg["logged_user"]
        logged = True if json_cfg["logged_user"] is not None else False

        currencies = json_data['Currencies']
        selected_wallet = ""

        if not logged:
            start_screen(json_data['Wallets'], json_cfg, json_passwords, json_data)
            user = json_cfg["logged_user"]
            dump_to_json("cfg", json_cfg)

        if user and json_cfg[user]["selected_wallet"]:
            selected_wallet = json_cfg[user]["selected_wallet"]

        if selected_wallet == "":
            print(f"Your wallets: {', '.join([w for w in json_data['Wallets'][user] if w != 'Password'])}")
            while True:
                selected_wallet = input("Please, select one of your wallets: ")
                if selected_wallet in json_data['Wallets'][user]:
                    print(f"Wallet {selected_wallet} selected!")
                    json_cfg[user]["selected_wallet"] = selected_wallet
                    dump_to_json("cfg", json_cfg)
                    break
                else:
                    print("ERROR: Invalid wallet! Try again.")

        choices(json_data['Wallets'], user, currencies, selected_wallet, json_cfg, logged, json_data, json_passwords)
        if not logged:
            break


if __name__ == "__main__":
    main()