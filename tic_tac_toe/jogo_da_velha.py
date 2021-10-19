from random import randint as rd
from random import choice
from emoji import emojize
from time import sleep as delay

layout = [
            [' ', 'O', ' ', '|', ' ', 'O', ' ', '|', ' ', 'O', ' '],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            [' ', 'O', ' ', '|', ' ', 'O', ' ', '|', ' ', 'O', ''],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            [' ', 'O', ' ', '|', ' ', 'O', ' ', '|', ' ', 'O', ' '],
        ]

win_positions = [
                    [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9],
                    [1, 5, 9],
                    [3, 5, 7],
                    [1, 4, 7],
                    [2, 5, 8],
                    [3, 6, 9]
                ]

game_layout =   [   
                    [
                        [' ', '1', ' ', '|', ' ', '2', ' ', '|', ' ', '3', ' '],
                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                        [' ', '4', ' ', '|', ' ', '5', ' ', '|', ' ', '6', ' '],
                        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                        [' ', '7', ' ', '|', ' ', '8', ' ', '|', ' ', '9', ' '],
                    ]
                ]

positions = {
                # Line 0
                '1' : [0, 1],
                '2' : [0, 5],
                '3' : [0, 9],

                # Line 2
                '4' : [2, 1],
                '5' : [2, 5],
                '6' : [2, 9],
                
                # Line 4
                '7' : [4, 1],
                '8' : [4, 5],
                '9' : [4, 9],
            }

player_choices = list()
cpu_choices = list()
to_win = list()
to_lose = list()
cpu_number = who_starts = tie = 0
who_turn = ''

win_msg = emojize(':trophy:')
lose_msg = '\U0001F622'
tie_msg = emojize(':unamused:')

#TODO: Testar algumas posições, mas a princípio a mecanica está respondendo ok
def result_msg(result):
    #print(f'CPU Moves {cpu_choices} | Player Moves {player_choices}')     
    print(result)

    while True:
        pass    

def player_turn():
    global player_choice, player_choices, who_turn, tie
    print('Player Turn')
    player_choice = int(input('Try a move: '))
    game_layout[0][positions[str(player_choice)][0]][positions[str(player_choice)][1]]
    while game_layout[0][positions[str(player_choice)][0]][positions[str(player_choice)][1]] == 'X' or game_layout[0][positions[str(player_choice)][0]][positions[str(player_choice)][1]] == 'O':
        print("This move isn't allowed", end='\n')
        player_choice = int(input('Try a move: '))
    if player_choice not in player_choices and player_choice not in cpu_choices:
        player_choices.append(player_choice)
        player_choices.sort()        
        game_layout[0][positions[str(player_choice)][0]][positions[str(player_choice)][1]] = 'X'
        tie += 1

def cpu_think():
    global cpu_number
    if len(cpu_choices) == 0:
        #print('cpu começou')
        cpu_number = rd (1, 9)
        
    if len(cpu_choices) > 0:
        print('len maior que 0')        
        if who_turn == 'p':
            if 1 not in cpu_choices and ((2 in player_choices and 3 in player_choices) or (4 in player_choices and 7 in player_choices) or (5 in player_choices and 9 in player_choices)):
                cpu_number = 1
            elif 2 not in cpu_choices and ((1 in player_choices and 3 in player_choices) or (5 in player_choices and 8 in player_choices)):
                cpu_number = 2
            elif 3 not in cpu_choices and ((1 in player_choices and 2 in player_choices) or (5 in player_choices and 7 in player_choices) or (6 in player_choices and 9 in player_choices)):
                cpu_number = 3
            elif 4 not in cpu_choices and ((1 in player_choices and 7 in player_choices) or (5 in player_choices and 6 in player_choices)):
                cpu_number = 4
            elif 5 not in cpu_choices and ((1 in player_choices and 7 in player_choices) or (1 in player_choices and 9 in player_choices) or (2 in player_choices and 8 in player_choices) or (3 in player_choices and 7 in player_choices) or (4 in player_choices and 6 in player_choices)):
                cpu_number = 5
            elif 6 not in cpu_choices and ((3 in player_choices and 9 in player_choices) or (4 in player_choices and 5 in player_choices)):    
                cpu_number = 6
            elif 7 not in cpu_choices and ((1 in player_choices and 4 in player_choices) or (3 in player_choices and 5 in player_choices) or (8 in player_choices and 9 in player_choices)):
                cpu_number = 7
            elif 8 not in cpu_choices and ((2 in player_choices and 5 in player_choices) or (7 in player_choices and 9 in player_choices)):
                cpu_number = 8
            elif 9 not in cpu_choices and ((1 in player_choices and 5 in player_choices) or (3 in player_choices and 6 in player_choices) or (7 in player_choices and 8 in player_choices)):
                cpu_number = 9
            elif 1 in player_choices and 3 in player_choices and 5 in player_choices:
                cpu_number = choice([2, 7, 9])
            elif 1 in player_choices and 3 in player_choices and 9 in player_choices:
                cpu_number = choice([2, 5, 6])
            elif 1 in player_choices and 3 in player_choices and 7 in player_choices:
                cpu_number = choice([2, 4, 5])
            elif 1 in player_choices and 7 in player_choices and 9 in player_choices:
                cpu_number = choice([4, 5, 8])
            elif 3 in player_choices and 7 in player_choices and 9 in player_choices:
                cpu_number = choice([5, 6, 8])

        elif who_turn == 'c':                
            if 1 not in cpu_choices and ((2 in cpu_choices and 3 in cpu_choices) or (5 in cpu_choices and 9 in cpu_choices) or (4 in cpu_choices and 7 in cpu_choices)):               
                cpu_number = 1
            elif 2 not in cpu_choices and ((1 in cpu_choices and 3 in cpu_choices) or (5 in cpu_choices and 8 in cpu_choices)):
                cpu_number = 2 
            elif 3 not in cpu_choices and ((1 in cpu_choices and 2 in cpu_choices) or (5 in cpu_choices and 7 in cpu_choices) or (6 in cpu_choices and 9 in cpu_choices)):
                cpu_number = 3
            elif 4 not in cpu_choices and ((2 in cpu_choices and 7 in cpu_choices) or (5 in cpu_choices and 6 in cpu_choices)):
                cpu_number = 4
            elif 5 not in cpu_choices and ((1 in cpu_choices and 9 in cpu_choices) or (2 in cpu_choices and 8 in cpu_choices) or (3 in cpu_choices and 8 in cpu_choices) or (4 in cpu_choices and 6 in cpu_choices)):
                cpu_number = 5
            elif 6 not in cpu_choices and ((3 in cpu_choices and 9 in cpu_choices) or (4 in cpu_choices and 5 in cpu_choices)):
                cpu_number = 6
            elif 7 not in cpu_choices and ((1 in cpu_choices and 4 in cpu_choices) or (3 in cpu_choices and 5 in cpu_choices) or (8 in cpu_choices and 9 in cpu_choices)):
                cpu_number = 7
            elif 8 not in cpu_choices and ((2 in cpu_choices and 5 in cpu_choices) or (7 in cpu_choices and 9 in cpu_choices)):
                cpu_number = 8
            elif 9 not in cpu_choices and ((1 in cpu_choices and 5 in cpu_choices) or (3 in cpu_choices and 6 in cpu_choices) or (7 in cpu_choices and 8 in cpu_choices)):
                cpu_number = 9

def cpu_turn():
    global cpu_number, cpu_choices, player_choices, who_turn, tie
    print('CPU Turn')    
            
    cpu_think()
    if len(cpu_choices) + len(player_choices) == 9:
        who_won()
    if cpu_number not in cpu_choices and cpu_number not in player_choices:
        cpu_choices.append(cpu_number)
        cpu_choices.sort()
        game_layout[0][positions[str(cpu_number)][0]][positions[str(cpu_number)][1]] = 'O'
    else:
        selected = cpu_choices.copy()
        selected.extend(player_choices)
        selected.sort()
        not_selected = list()
        for num in range(1, 10, 1):
            for item in selected:
                if num in selected:
                    #print('já existe', num)
                    break
                else:
                    #print('não existe', num)
                    not_selected.append(num)
                    break
        not_selected.sort()
        cpu_number = choice(not_selected)
        #print(not_selected)
        game_layout[0][positions[str(cpu_number)][0]][positions[str(cpu_number)][1]] = 'O'
    tie += 1
                        
    
def print_layout():    
    for x in range(len(game_layout[0])):
        print(end='\n')
        for y in range(len(game_layout[0][x])):                            
            print(game_layout[0][x][y], end='')
    print(end='\n')
    
def who_won():
    global who_turn
    # Verifica as posições de win
    if tie > 8:
        print("IT'S A TIE")
        result_msg(tie_msg)
    else:
        to_win.clear()
        for pos, item in enumerate(win_positions):    
            for x in player_choices:
                for y in range(len(win_positions[pos])):
                    if x == win_positions[pos][y]:
                        to_win.append(pos)
        for x in to_win:
            if to_win.count(x) >= 1:
                who_turn = 'p'
            if to_win.count(x) == 3:
                print('You WIN')
                result_msg(win_msg)
            #print(to_win.count(x), end='P| ')
        #print(who_turn)
        #print(f'TIE? {tie}')

        to_lose.clear()   
        for pos, item in enumerate(win_positions):    
            for x in cpu_choices:
                for y in range(len(win_positions[pos])):
                    if x == win_positions[pos][y]:
                        to_lose.append(pos)
        for x in to_lose: 
            if to_lose.count(x) > 1:
                who_turn = 'c'
            if to_lose.count(x) == 3:                    
                print('CPU WINS')
                result_msg(lose_msg)
            #print(to_lose.count(x), end='C| ')

                
def game():    
    global my_sum, cpu_sum, who_turn
    who_starts = rd(0, 1)
    while True:
        #print(f'TIE: {tie}')      
        if who_starts == 0:
            who_won()
            player_turn()
            who_won()
            cpu_turn()
            who_won()                
            print_layout()
        else:
            who_won()
            cpu_turn()
            who_won()
            print_layout()
            who_won()
            player_turn()
            who_won()
            print_layout()        
            
game()

cpu_choices = [1, 2]
while True:
    
    selected = cpu_choices.copy()
    selected.extend(player_choices)
    selected.sort()
    not_selected = list()
    print(selected)

    for num in range(1, 10, 1):
        for item in selected:
            if num in selected:
                print('já existe', num)
                break
            else:
                print('não existe', num)
                not_selected.append(num)
                break
    not_selected.sort()