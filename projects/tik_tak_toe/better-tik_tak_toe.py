from time import sleep
from random import randint
from datetime import datetime

cells = {
    "num7": [" ", 7],
    "num8": [" ", 8],
    "num9": [" ", 9],

    "num4": [" ", 4],
    "num5": [" ", 5],
    "num6": [" ", 6],

    "num1": [" ", 1],
    "num2": [" ", 2],
    "num3": [" ", 3]
}



stats = []

game_running = False
win = False
gamemode_1 = False
gamemode_2 = False
is_pc_move = False

player_now = "X"
choice = None
pc_figure = None
figure = None
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

numpad = True

x_wins = 0
o_wins = 0
draws = 0


def write_in_file():
    with open("logs.txt", "a") as file:
        file.write(f'[{current_time}] Wins X: {x_wins}. Wins O: {o_wins}. Draws: {draws}.   Gamemode: {"PvP" if gamemode == "end_1" else f"PvC    Player: {figure}"}\n')


def render_field():
    print("Rendering field")
    print(f"{cells['num7'][0]} | {cells['num8'][0]} | {cells['num9'][0]}")
    print("---------")
    print(f"{cells['num4'][0]} | {cells['num5'][0]} | {cells['num6'][0]}")
    print("---------")
    print(f"{cells['num1'][0]} | {cells['num2'][0]} | {cells['num3'][0]}\n")


def change_player():
    print("Changing player")
    global player_now
    if player_now == "X":
        player_now = "O"
    else:
        player_now = "X"


def check_win():
    print("Checking win")
    global player_now, win, cells, gamemode
    winning_combinations = [
        [cells["num7"], cells["num8"], cells["num9"]],  # Top row
        [cells["num4"], cells["num5"], cells["num6"]],  # Middle row
        [cells["num1"], cells["num2"], cells["num3"]],  # Bottom row

        [cells["num7"], cells["num4"], cells["num1"]],  # Left column
        [cells["num8"], cells["num5"], cells["num2"]],  # Middle column
        [cells["num9"], cells["num6"], cells["num3"]],  # Right column

        [cells["num7"], cells["num5"], cells["num3"]],  # Diagonal
        [cells["num9"], cells["num5"], cells["num1"]]  # Diagonal
    ]

    for combination in winning_combinations:
        if combination[0][0] == combination[1][0] == combination[2][0] == player_now:
            stats.append(player_now)
            print(f"{player_now} виграв!")
            win = True
            return

    if all(cell[0] != " " for cell in cells.values()):
        stats.append("draw")
        print("Нічия!")
        win = True

    if win:
        choice = input("Ви бажаєте зіграти ще раз?").lower()
        if choice == "так":
            cells = {key: [" ", value[1]] for key, value in cells.items()}  # Так зробити мені підказав ChatGPT
            win = False
        else:
            gamemode = "end_1" if gamemode == 1 else "end_2"


def player_move():
    print("Moving player")
    while True:
        try:
            choice = int(
                input(f"Зараз ходить {player_now}!\nВиберіть клітину {"(NumPad 7-3)" if numpad else "(1-9)"}: \n"))
        except ValueError:
            print("Будь ласка, введіть число.")
            continue

        if 1 <= choice <= 9:
            if cells[f"num{choice}"][0] == " ":
                cells[f"num{choice}"][0] = player_now
                render_field()
                break
            else:
                print("\nЦя клітина вже зайнята, виберіть іншу.\n")
        else:
            print("Невірний вибір! Виберіть число від 1 до 9.")


def pc_move():
    print("Moving pc")
    for i in range(1, 4):
        if cells[f"num{i}"][0] == cells[f"num{i + 3}"][0] == pc_figure and cells[f"num{i + 6}"][0] == " ":
            cells[f"num{i + 6}"][0] = pc_figure
            print(1)
            return
        elif cells[f"num{i + 3}"][0] == cells[f"num{i + 6}"][0] == pc_figure and cells[f"num{i}"][0] == " ":
            cells[f"num{i}"][0] = pc_figure
            print(2)
            return
        elif cells[f"num{i}"][0] == cells[f"num{i + 6}"][0] == pc_figure and cells[f"num{i + 3}"][0] == " ":
            cells[f"num{i}"][0] = pc_figure
            print(3)
            return

    while True:
        choice = randint(1, 9)

        if cells[f"num{choice}"][0] == " ":
            cells[f"num{choice}"][0] = pc_figure
            print("Random")
            return


def pick_figure():
    global figure, pc_figure
    figure = input("Виберіть фігуру (X, O)").upper()

    if figure == "X":
        pc_figure = "O"
    else:
        pc_figure = "X"

    while "X" != figure != "O":
        figure = input("Введіть X або O!").upper()
    sleep(0.5)


def changing_logic():
    if player_now == figure:
        player_move()
    else:
        pc_move()


while True:
    if win: break

    print("Вітаю в грі \"Хрестики нулики\"!")
    sleep(0.5)
    print(f"\nВ грі можна грати з комп'ютером або вдвох.\n\nПравила прості:\nВи вводите номер клітини в яку хочете "
          f"поставити свою фігуру (1 - 9 або 7 - 3)")
    input("Натисніть Enter щоб продовжити...")

    # numpad = input("Виберіть режим:\n1 - NumPad\n2 - Числовий рядок\n")
    # numpad = True if numpad == '1' else False if numpad == '2' else None
    # while numpad is None:
    #     numpad = input("Невірний вибір! Будь ласка, введіть 1 або 2.")
    #     numpad = True if numpad == '1' else False if numpad == '2' else None
    # sleep(0.5)

    gamemode = int(input("Виберіть режим гри:\nВдвох - 1\nЗ комп'ютером - 2\n"))
    while 1 != gamemode != 2:
        gamemode = input("Введіть 1 або 2!")
    sleep(0.5)

    while gamemode == 1:
        render_field()
        player_move()
        check_win()
        change_player()

    while gamemode == 2:
        if figure is not None:
            render_field()
            changing_logic()
            check_win()
            change_player()
        else:
            pick_figure()

for wins in stats:
    if wins == "X":
        x_wins += 1
    elif wins == "O":
        o_wins += 1
    elif wins == "draw":
        draws += 1

print(f"Статистика гри:\nВиграшів Х: {x_wins}\nВиграшів О: {o_wins}\nНічий: {draws}")
write_in_file()