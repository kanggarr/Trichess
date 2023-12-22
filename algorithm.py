import random
import time

def algorithm_provider(possible_move, current_board, type_algorithm):
    if type_algorithm == 1:
        return play_random(possible_move)
    elif type_algorithm == 2:
        return testalgo2(possible_move, current_board)


    # handle any algorithm
    else:
        return play_random(possible_move)
    

def play_random(possible_move):
    while True:
        try:
            print("This is possible move: ", possible_move)

            random_piece = random.choice(list(possible_move.keys()))
            random_move = random.choice(possible_move[random_piece])
            
            print(possible_move)
            print(list(possible_move.keys()))
            print(possible_move.keys())

            print(f"This is random piece: {random_piece} and random move: {random_move}")

            return random_piece, random_move
        except:
            pass
        time.sleep(1)

def testalgo(possible_move, current_board):
    targetvalue_chess = {'Pawn':1, 'Knight':3, 'Bishop':3, 'Rocok':5, 'Queen':9, 'King':99}
    value_chess = {'Pawn':1, 'Knight':3, 'Bishop':3, 'Rocok':5, 'Queen':9, 'King':99}
    top = 0
    try:
        print("This is possible move: ", possible_move)
        for p, m in possible_move.items():
            for move in m:
                if move in [entry['Field'] for entry in current_board]:
                    random_piece = p
                    random_move = move
                    return random_piece, random_move
            return play_random(possible_move)
    except:
        pass
    time.sleep(1)

def testalgo2(possible_move, current_board):
    targetvalue_chess = {'Pawn':1, 'Knight':3, 'Bishop':3, 'Rocok':5, 'Queen':9, 'King':99}
    value_chess = {'Pawn':1, 'Knight':3, 'Bishop':3, 'Rocok':5, 'Queen':9, 'King':99}
    top = 0
    try:
        print("This is possible move: ", possible_move)
        for p, m in possible_move.items():
            for move in m:
                if move in [entry['Field'] for entry in current_board]:
                    random_piece = p
                    random_move = move
                    return random_piece, random_move
            return play_random(possible_move)
    except:
        pass
    time.sleep(1)


