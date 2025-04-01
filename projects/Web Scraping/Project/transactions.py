from hashlib import sha256

def check_login(logged: bool) -> bool:
    if logged: return True
    return False

def request_password(username: str, users_db: dict, logged: bool) -> bool:
    if check_login(logged) is not True:
        return False

    password = input("Enter your password: ")
    password = sha256(password.encode()).hexdigest()

    if users_db[username] == password:
        return True
    return False

def transaction(users_db: dict, balances_db: dict, username: str, logged: bool, safe_transactions: bool) -> bool:
    if not check_login(logged):
        return False

    while True:
        transaction_type = input("What type of transaction do you want to make?\n1 - Transfer to card\n2 - IBAN")

        if transaction_type in ("1", "2"):
            break

    if transaction_type == "1":
        receiver = input("Enter the recipient's username: ")

        if receiver not in users_db:
            print("Invalid username!")
            return False

    else:
        receiver = input