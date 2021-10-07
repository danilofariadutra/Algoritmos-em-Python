from random import randint as rd
from emoji import emojize

minesweeper = list()
mine_positions = list()
player_positions = list()
zero_positions = list()
horizon_left = [9, 18, 27, 36, 45, 54, 63, 72]
horizon_right = [8, 17, 26, 35, 44, 53, 62, 71, 80]

mine = list()
mine_layout = list()

game_over = False

zero = emojize(':keycap_0:')
one = emojize(':keycap_1:')
two = emojize(':keycap_2:')
three = emojize(':keycap_3:')
four = emojize(':keycap_4:')
five = emojize(':keycap_5:')
question = emojize(':white_question_mark:')
bomb = emojize(':bomb:')
win = emojize(':trophy:')


def randomize_bomb_positions():
    while True:
        if len(mine_positions) == 10:
            break
        bomb = rd(1, 81)
        if bomb not in mine_positions:
            mine_positions.append(bomb)
        mine_positions.sort()

    for pos in range(81):
        if pos < 81:
            if pos not in mine_positions:
                minesweeper.append('0')
            else:
                minesweeper.append('-1')


def check_how_many_mines():
    for pos in range(len(minesweeper)):
        if pos == 0:
            if minesweeper[pos + 1] == '-1':
                mine.append(pos)
            if minesweeper[pos + 9] == '-1':
                mine.append(pos)
            if minesweeper[pos + 10] == '-1':
                mine.append(pos)
        if pos != 0 and pos not in mine_positions and pos not in horizon_left and pos not in horizon_right and pos < 9:
            if minesweeper[pos - 1] == '-1':
                mine.append(pos)
            if minesweeper[pos + 1] == '-1':
                mine.append(pos)
            if minesweeper[pos + 8] == '-1':
                mine.append(pos)
            if minesweeper[pos + 9] == '-1':
                mine.append(pos)
            if minesweeper[pos + 10] == '-1':
                mine.append(pos)
        elif pos != 0 and pos not in mine_positions and pos not in horizon_left and pos not in horizon_right and (pos > 9 and pos < len(minesweeper) - 10):
            if minesweeper[pos - 1] == '-1':
                mine.append(pos)
            if minesweeper[pos + 1] == '-1':
                mine.append(pos)
            if minesweeper[pos - 8] == '-1':
                mine.append(pos)
            if minesweeper[pos - 9] == '-1':
                mine.append(pos)
            if minesweeper[pos - 10] == '-1':
                mine.append(pos)
            if minesweeper[pos + 8] == '-1':
                mine.append(pos)
            if minesweeper[pos + 9] == '-1':
                mine.append(pos)
            if minesweeper[pos + 10] == '-1':
                mine.append(pos)
        elif pos != 0 and pos not in mine_positions and pos not in horizon_left and pos not in horizon_right and pos > (len(minesweeper) - 10):
            if minesweeper[pos - 1] == '-1':
                mine.append(pos)
            if minesweeper[pos + 1] == '-1':
                mine.append(pos)
            if minesweeper[pos - 8] == '-1':
                mine.append(pos)
            if minesweeper[pos - 9] == '-1':
                mine.append(pos)
            if minesweeper[pos - 10] == '-1':
                mine.append(pos)

        if pos in horizon_right and pos not in mine_positions:
            if pos == 8:
                if minesweeper[pos - 1] == '-1':
                    mine.append(pos)
                if minesweeper[pos + 8] == '-1':
                    mine.append(pos)
                if minesweeper[pos + 9] == '-1':
                    mine.append(pos)
            if pos == 80 and pos not in mine_positions:
                if minesweeper[pos - 1] == '-1':
                    mine.append(pos)
                if minesweeper[pos - 9] == '-1':
                    mine.append(pos)
                if minesweeper[pos - 10] == '-1':
                    mine.append(pos)
            else:
                if pos != 8:
                    if minesweeper[pos - 1] == '-1':
                        mine.append(pos)
                    if minesweeper[pos + 8] == '-1':
                        mine.append(pos)
                    if minesweeper[pos + 9] == '-1':
                        mine.append(pos)
                    if minesweeper[pos - 9] == '-1':
                        mine.append(pos)
                    if minesweeper[pos - 10] == '-1':
                        mine.append(pos)
        if pos in horizon_left and pos not in mine_positions:
            if pos == 72 and pos not in mine_positions:
                if minesweeper[pos + 1] == '-1':
                    mine.append(pos)
                if minesweeper[pos - 8] == '-1':
                    mine.append(pos)
                if minesweeper[pos - 9] == '-1':
                    mine.append(pos)
            else:
                if minesweeper[pos + 1] == '-1':
                    mine.append(pos)
                if minesweeper[pos + 9] == '-1':
                    mine.append(pos)
                if minesweeper[pos + 10] == '-1':
                    mine.append(pos)
                if minesweeper[pos - 8] == '-1':
                    mine.append(pos)
                if minesweeper[pos - 9] == '-1':
                    mine.append(pos)


def create_layout():
    for pos in range(len(minesweeper)):
        mine_layout.append(str(mine.count(pos)))


def player():
    global game_over
    while True:
        player_choice = input('Choose a position: ')
        if player_choice.isnumeric():
            player_choice = int(player_choice) - 1
        else:
            while player_choice.isnumeric() is False:
                player_choice = input(
                    "This positions isn't numeric. Please choose again: ")
                if player_choice.isnumeric():
                    player_choice = int(player_choice) - 1
                    break

        if player_choice not in player_positions:
            player_positions.append(player_choice)
            break
        else:
            player_positions.sort()
            print(f'Positions not available: [{player_positions}]')

    if mine_layout[player_choice] == '-1':
        game_over = True
        print('\n')
        print('          KABUUUUUUUUUUUUUM')
        print(f'          {bomb} GAME OVER! {bomb}')
        print('\n')
        print_layout()
    elif len(player_positions) >= 71:
        game_over = True
        print('\n')
        print('          WOOOOOOOOOOOOOW')
        print('          CONGRATULATIONS')
        print(f'          {win} YOU WIN! {win}')
        print('\n')


def print_layout():
    while True:
        counter = 0
        print('     ', end='')
        for pos_x in range(9):
            print(f' {pos_x + 1} ', end='')
        print(end='\n')
        print('_' * 37)

        for pos_y in range(9):
            if counter < 9:
                print(f' 0{pos_y + 1}| ', end='')
            else:
                print(f' {(pos_y * 9) + 1}| ', end='')

            for pos_y in range(9):
                if counter in mine_positions:
                    mine_layout[counter] = '-1'
                else:
                    mine_layout.append(str(mine.count(pos_x)))

                if counter not in player_positions and game_over is False:
                    print(f' {question}', end='')
                else:
                    if mine_layout[counter] == '-1':
                        print(f' {bomb}', end='')
                    elif mine_layout[counter] == '0':
                        print(f' {zero} ', end='')
                        for pos in range(counter, len(mine_layout), 1):
                            if mine_layout[pos] == '0':
                                if pos not in player_positions and pos < 81:
                                    player_positions.append(pos)
                                    player_positions.sort()
                            else:
                                break

                    elif mine_layout[counter] == '1':
                        print(f' {one} ', end='')
                    elif mine_layout[counter] == '2':
                        print(f' {two} ', end='')
                    elif mine_layout[counter] == '3':
                        print(f' {three} ', end='')
                    elif mine_layout[counter] == '4':
                        print(f' {four} ', end='')
                    elif mine_layout[counter] == '5':
                        print(f' {five} ', end='')
                counter += 1
            print(f'| {counter}', end='')
            print(end='\n')

        if game_over == True:
            while True:
                pass

        player()


def game():
    if __name__ == '__main__':
        randomize_bomb_positions()
        check_how_many_mines()
        create_layout()
        print_layout()


game()
