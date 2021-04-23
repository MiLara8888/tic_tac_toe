def board(x):
    print('_' * 13)
    for i in range(3):
        print('|', x[0 + (i * 3)], '|', x[1 + (i * 3)], '|', x[2 + (i * 3)], '|')
    print('-' * 13)


board1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def game_x(n):
    board1[n - 1] = 'X'
    board(board1)


def game_o(n):
    board1[n - 1] = '0'
    board(board1)


def check(n):
    if board1[n - 1] != 'X' and board1[n - 1] != '0':
        return True
    else:
        return False


def win(d):
    list = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for i in list:
        if board1[i[0]] == board1[i[1]] == board1[i[2]]:
            return True

    return False


count = 1

board(board1)
while True:
    flag = True
    if count % 2 != 0:
        print('Xoдит крестик')
        while flag:
            try:
                m = int(input('Крестик-введите клетку поля-'))
            except:
                print("Введите число")
                continue
            if 1 < m > 9:
                print('Нет такого поля!')
                continue

            if check(m):
                flag = False
            else:
                print('Клетка занята!')

        game_x(m)
        if win(board1):
            print('\033[33mВыиграл- крестик!')
            break

    elif count % 2 == 0:
        print('Ходит нолик')
        while flag:
            try:
                m = int(input('Нолик-введите клетку поля-'))
            except:
                print('Введите число')
                continue
            if 1 < m > 9:
                print('Нет такого поля')
                continue
            if check(m):
                flag = False
            else:
                print('Клетка занята!')
        game_o(m)
        if win(board1):
            print('Выиграл нолик!')
            break
    count += 1
