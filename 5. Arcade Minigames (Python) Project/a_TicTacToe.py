import random

spots = {1: ' 1 ', 2: ' 2 ', 3: ' 3 ', 4: ' 4 ', 5: ' 5 ', 6: ' 6 ', 7: ' 7 ', 8: ' 8 ', 9: ' 9 '}

def main(): 

    print('Welcome to a game of Tic Tac Toe! (User vs CPU)\n')
    print('Select a position by typing the corresponding number!')
    draw_board(spots)

    playing = True

    while playing:
        x = user_play()
        spots[int(x)] = ' O '
        draw_board(spots)

        if user_winner(spots) is True:
            break

        if full_board() is True:
            print("Its a tie!")
            break

        y = computer_play()
        spots[int(y)] = ' X '
        print(f"Computer chose: {y}")
        draw_board(spots)

        if CPU_winner(spots) is True:
            break

        if full_board() is True:
            print("Its a tie!")
            break


def user_play():
    while True:
        try: 
            n = input("Choose position: ")
            if spots[int(n)] in [' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 ']:
                break
        except Exception:
            print("That position is not available!")
    return n
    

def computer_play():
    while True:
        try: 
            n = random.randint(1, 9)
            if spots[int(n)] in [' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 ']:
                break
        except Exception:
            print("That position is not available!")
    return n


def user_winner(spots):
    if spots[1] == ' O ' and spots[2] == ' O ' and spots[3] == ' O ':
        print("You won!")
        return True 
    if spots[4] == ' O ' and spots[5] == ' O ' and spots[6] == ' O ':
        print("You won!")
        return True 
    if spots[7] == ' O ' and spots[8] == ' O ' and spots[9] == ' O ':
        print("You won!")
        return True 
    if spots[1] == ' O ' and spots[5] == ' O ' and spots[9] == ' O ':
        print("You won!")
        return True 
    if spots[3] == ' O ' and spots[5] == ' O ' and spots[7] == ' O ':
        print("You won!")
        return True  
    if spots[1] == ' O ' and spots[4] == ' O ' and spots[7] == ' O ':
        print("You won!")
        return True 
    if spots[2] == ' O ' and spots[5] == ' O ' and spots[8] == ' O ':
        print("You won!")
        return True 
    if spots[3] == ' O ' and spots[6] == ' O ' and spots[9] == ' O ':
        print("You won!")
        return True
    return False


def CPU_winner(spots):
    if spots[1] == ' X ' and spots[2] == ' X ' and spots[3] == ' X ':
        print("You lost!")
        return True 
    if spots[4] == ' X ' and spots[5] == ' X ' and spots[6] == ' X ':
        print("You lost!")
        return True 
    if spots[7] == ' X ' and spots[8] == ' X ' and spots[9] == ' X ':
        print("You lost!")
        return True 
    if spots[1] == ' X ' and spots[5] == ' X ' and spots[9] == ' X ':
        print("You lost!")
        return True 
    if spots[3] == ' X ' and spots[5] == ' X ' and spots[7] == ' X ':
        print("You lost!")
        return True 
    if spots[1] == ' X ' and spots[4] == ' X ' and spots[7] == ' X ':
        print("You lost!")
        return True 
    if spots[2] == ' X ' and spots[5] == ' X ' and spots[8] == ' X ':
        print("You lost!")
        return True 
    if spots[3] == ' X ' and spots[6] == ' X ' and spots[9] == ' X ':
        print("You lost!")
        return True 
    return False

def full_board():
    if (spots[1] == (' X ') or spots[1] == (' O ')) and (spots[2] == (' X ') or spots[2] == (' O '))  and (spots[3] == (' X ') or spots[3] == (' O '))  and (spots[4] == (' X ') or spots[4] == (' O '))  and (spots[5] == (' X ') or spots[5] == (' O '))  and (spots[6] == (' X ') or spots[6] == (' O '))  and (spots[7] == (' X ') or spots[7] == (' O '))  and (spots[8] == (' X ') or spots[8] == (' O '))  and (spots[9] == (' X ') or spots[9] == (' O ')) :
        return True
    return False

def draw_board(spots):
    print(f"{spots[1]},{spots[2]},{spots[3]}\n{spots[4]},{spots[5]},{spots[6]}\n{spots[7]},{spots[8]},{spots[9]}")
