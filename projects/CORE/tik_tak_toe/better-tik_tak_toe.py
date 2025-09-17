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
pc_moved = False

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
        file.write(f'[{current_time}] Wins X: {x_wins}. Wins O: {o_wins}. Draws: {draws}.   Gamemode: {"PvP" if gamemode == "end_1" else f"PvC.    Player: {figure}"}\n')


def render_field():
    print(f" {cells['num7'][0]} | {cells['num8'][0]} | {cells['num9'][0]} ")
    print("___|___|___")
    print(f" {cells['num4'][0]} | {cells['num5'][0]} | {cells['num6'][0]} ")
    print("___|___|___")
    print(f" {cells['num1'][0]} | {cells['num2'][0]} | {cells['num3'][0]} ")
    print("   |   |   \n")


def change_player():
    global player_now
    if player_now == "X":
        player_now = "O"
    else:
        player_now = "X"


def check_win():
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

    if all(cell[0] != " " for cell in cells.values()):
        stats.append("draw")
        print("Нічия!")
        win = True

    if win:
        choice = input("Ви бажаєте зіграти ще раз?").lower()
        if choice == "так":
            cells = {key: [" ", value[1]] for key, value in cells.items()}
            player_now = "X"
            win = False
            render_field()
        else:
            gamemode = "end_1" if gamemode == "1" else "end_2"


def player_move():
    while True:
        try:
            choice = int(
                input(f"Зараз ходить {player_now}!\nВиберіть клітину {'(NumPad 7-3)' if numpad else '(1-9)'}: \n"))
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
    sleep(0.5)

def pc_move(): # Я вже не знав що робити, і запитав у чата гпт. Я наче зрозумів логіку цієї функції як він її написав
    global pc_moved
    for combo in [
        ["num7", "num8", "num9"], ["num4", "num5", "num6"], ["num1", "num2", "num3"],
        ["num7", "num4", "num1"], ["num8", "num5", "num2"], ["num9", "num6", "num3"],
        ["num7", "num5", "num3"], ["num9", "num5", "num1"]
    ]:
        line = [cells[pos][0] for pos in combo]
        if line.count(pc_figure) == 2 and line.count(" ") == 1:
            cells[combo[line.index(" ")]][0] = pc_figure
            pc_moved = True
            render_field()
            return
        if line.count(figure) == 2 and line.count(" ") == 1:
            cells[combo[line.index(" ")]][0] = pc_figure
            pc_moved = True
            render_field()
            return

    while not pc_moved:
        choice = f"num{randint(1, 9)}"
        if cells[choice][0] == " ":
            cells[choice][0] = pc_figure
            pc_moved = True
            render_field()
            break
    pc_moved = False


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
          f"поставити свою фігуру (NumPad 7 - 3)")
    input("Натисніть Enter щоб продовжити...")

    gamemode = input("Виберіть режим гри:\nВдвох - 1\nЗ комп'ютером - 2\n")
    while "1" != gamemode != "2":
        gamemode = input("Введіть 1 або 2!")
    sleep(0.5)
    render_field()

    while gamemode == "1":
        player_move()
        check_win()
        render_field()
        change_player()

    while gamemode == "2":
        if figure is not None:
            changing_logic()
            check_win()
            render_field()
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
