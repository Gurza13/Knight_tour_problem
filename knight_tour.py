# Правило Варнсдорфа / The Warnsdorf Rule

import random


# генерация доски / generating a board
board = [x * 10 + y for x in range(8,0,-1) for y in range(1,9)]

# алгоритм ходов конем / knight's move algorithm
steps_knight = [21, 19, 12, 8, -8, -12, -19, -21]

# начальное поле доски / the initial field of the board
start_cell = random.choice([10 * (y + 1) + (x + 1) for y in range(8) for x in range(8)])
board.remove(start_cell)

chess_board = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h'}

k = 1
print('Ход ', k, ' - ', chess_board[int(str(start_cell)[-1])],int(str(start_cell)[0]), sep='')

while len(board)>0:

    # количество ходов из текущего поля / the number of moves from the current field
    steps_quantity = [start_cell + item for item in steps_knight if start_cell + item in board]

    # последующее количество ходов из каждого поля / the subsequent number of moves from each field
    var = []
    for i in steps_quantity:
        possible_steps = [i + item for item in steps_knight if i + item in board]
        var.append(len(possible_steps))

    # определение минимального количества ходов из последующих полей / determining the minimum number of moves from the following fields
    # список индексов минимальных значений / list of minimum value indexes
    lst_random_step = [j for j, item in enumerate(var) if item == min(var)]
    # выбор случайного числа из списка / choosing a random number from the lis
    random_step = random.choice(lst_random_step)
    # переход на новое поле / switching to a new field
    start_cell = steps_quantity[random_step]
    k += 1

    print('Ход ', k, ' - ', chess_board[int(str(start_cell)[-1])],int(str(start_cell)[0]), sep='')
    board.remove(start_cell)

print('Всего шагов:', k)
