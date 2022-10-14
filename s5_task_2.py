'''
Создайте программу для игры в ""Крестики-нолики"".
'''
desk = [1,2,3,4,5,6,7,8,9]


def print_desk():
    print("-" *18)
    for i in range(3):
        for j in range(3):
            print(f'{desk[j+i*3]:^5}', end=" ")
        print(f'\n{"-" *18}')
    print()

def players_step(step, symbol):
    play = desk.index(step)
    desk[play] = symbol

def is_win():
    win_combo = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    w = ""
    for i in win_combo:
        if desk[i[0]] == "X" and desk[i[1]] == "X" and desk[i[2]] =="X": w = "Игрок 1 (X)"
        if desk[i[0]] == "O" and desk[i[1]] == "O" and desk[i[2]] =="O": w = "Игрок 2 (O)"  
    return w

finish = False
first_player = True
count = 0
while finish == False:
    print_desk()
    if first_player == True:
        symbol = "X"
    else:
        symbol = "O"
    step = int(input("Сделайте ход: "))
    if step in range(1,10):
        players_step(step,symbol)
    else: print("Введено неверное значение")
    if count > 3:
        if is_win():
            print(f"{is_win()} - ПОБЕДИЛ!")
            break
        if count == 8:
            print("Все проиграли.")
            break
    count+=1
    print(count)
    first_player = not(first_player)
