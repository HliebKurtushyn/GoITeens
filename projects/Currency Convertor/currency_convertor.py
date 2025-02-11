currencies = {
    "USD": {"buy": 41.92, "sell": 41.48},
    "EUR": {"buy": 43.61, "sell": 43.66},
    "PLN": {"buy": 10.34, "sell": 10.21},
    "CZK": {"buy": 1.73, "sell": 1.50},
    "GBP": {"buy": 52.09, "sell": 51.98}
}

wallets = {
    "User1": {"Wallet1": {"UAH": 1057.0}, "Wallet2": {"UAH": 17.0}, "Password": "1234"},
    "User2": {"Wallet1": {"UAH": 56.0}, "Wallet2": {}, "Password": "123456"},
}

user = None
selected_wallet = None
logged = False


def convert(count=1.0):
    print(f"{count} UAH in other currencies:")
    for currency, rates in currencies.items():
        buy_rate = rates["buy"]
        sell_rate = rates["sell"]
        print(f"    {currency}:    BUY: {count / buy_rate:.2f} | SELL: {count / sell_rate:.2f}")


def convert_your_wallet():
    if user in wallets and selected_wallet in wallets[user]:
        balance = wallets[user][selected_wallet].get("UAH", 0)
        print(f"Your converted wallet ({selected_wallet}):")
        print(f"  UAH: {balance}")

        for currency, rates in currencies.items():
            buy_rate = rates["buy"]
            print(f"    {currency}: {balance / buy_rate:.2f}")

    else:
        print(f"Wallet '{selected_wallet}' not found for user '{user}'.")


def add_new_wallet(name="New Wallet"):
    if user in wallets:
        wallets[user][name] = {}
        return "Wallet has been successfully added" if name in wallets[user] else "Something went wrong"
    else:
        return "User {user} not found"


def deposit():
    if user in wallets and selected_wallet in wallets[user]:
        while True:
            dep_currency = input("Enter amount which you want to deposit (MAX '100.000 UAH'):\n   ")

            try:
                dep_currency = float(dep_currency)
            except ValueError:
                print("ERROR: Please, enter a valid number!")
                continue

            if 0.0 < dep_currency <= 100000.0:
                wallets[user][selected_wallet]["UAH"] += dep_currency
                print(f"{dep_currency:.2f} successfully added to {user}'s {selected_wallet}")
                break
            else:
                print("ERROR: Number must be between 0 and 100.000 UAH!")
    else:
        print("User or wallet is not found")


def withdraw():
    if user in wallets and selected_wallet in wallets[user]:
        while True:
            withdraw_currency = input("Enter amount which you want to withdraw (MAX '100.000 UAH'):\n   ")

            try:
                withdraw_currency = float(withdraw_currency)
            except ValueError:
                print("ERROR: Please, enter a valid number!")
                continue

            if wallets[user][selected_wallet].get("UAH", 0) < withdraw_currency:
                print("ERROR: Not enough money on your balance!")
                continue

            if 0.0 < withdraw_currency <= 100000.0:
                wallets[user][selected_wallet]["UAH"] -= withdraw_currency
                print(f"{withdraw_currency:.2f} successfully withdrawn from {user}'s {selected_wallet}")
                break
            else:
                print("ERROR: Number must be between 0 and 100.000 UAH!")
    else:
        print("User or wallet is not found")


def log_in():
    global user, logged
    while not logged:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in wallets and wallets[username]["Password"] == password:
            print(f"Successfully logged in as {username}!")
            user = username
            logged = True
            return True
        else:
            print("ERROR: Invalid username or password!")


while True:
    if not logged:
        log_in()

    if selected_wallet is None:
        print(f"Your wallets: {', '.join([w for w in wallets[user] if w != 'Password'])}")
        while True:
            selected_wallet = input("Please, select one of your wallets: ")
            if selected_wallet in wallets[user]:
                print(f"Wallet {selected_wallet} selected!")
                break
            else:
                print("ERROR: Invalid wallet! Try again.")

    print("\nChoose an action:")
    print("1. Select wallet")
    print("2. Convert UAH")
    print("3. Convert your wallet balance")
    print("4. Deposit money")
    print("5. Withdraw money")
    print("6. Exit")

    choice = input(": ")

    if choice == "1":
        while True:
            print(f"Your wallets: {', '.join([w for w in wallets[user] if w != 'Password'])}")
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
            convert(amount)
        except ValueError:
            print("ERROR: Please enter a valid number!")

    elif choice == "3":
        convert_your_wallet()

    elif choice == "4":
        deposit()

    elif choice == "5":
        withdraw()

    elif choice == "6":
        print("Exit...")
        print("ПРОГРАМА ГОТОВА ЛИШЕ ДЛЯ ПОКАЗУ. В НАЙБЛИЖЧОМУ МАЙБУТНЬОМУ Я ЇЇ ЗРОБЛЮ ЯК СВІЙ ОСОБИСТИЙ ПОВНОЦІННИЙ ПРОЕКТ")
        break

    else:
        print("ERROR: Invalid choice! Try again.")
