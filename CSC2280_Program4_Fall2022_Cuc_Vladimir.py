import random
#importing the random for our random things

def print_board(Matrix):
    #this function prints our Matrix where our table is saved
    #along with the demonstration table showing where each number coresponds to
    n = 1
    for i in range(3):
        print("|---+---+---|   |---+---+---|")
        print("|", end="")
        for j in range(3):
            print(f" {Matrix[i][j]} |", end='')
        print("   |", end="")
        for j in range(3):
            print(f" {n} |", end='')
            n += 1
        print("")
    print("|---+---+---|   |---+---+---|")

def is_digit(choice):
    #this function checks if the a choice is a number
    #if it's not return a message

    if choice.isdigit():
        return True
    else:
        print(" -----------------------")
        print("| Please insert a digit |")
        print(" -----------------------")
        return False

def main_is_in_between(choice, limit):
    #this function checks if a number is between 1 and a limit
    #if it's not return a message

    if choice >= "1" and int(choice) <= 5:
        return True
    else:
        print(" ----------------------------------------")
        print(f"| Please insert a number between 1 and {limit} |")
        print(" ----------------------------------------")
        return False
def dif_is_in_between(dif_choice):
    #this function checks if the difficulty choice is between 1 and 5
    #if it's not return a message
    if dif_choice >= "1" and dif_choice <= "5":
        return True
    else:
        print(" ----------------------------------------")
        print("| Please insert a number between 1 and 5 |")
        print(" ----------------------------------------")
        return False

def movement_is_in_between(move):
    # this function checks if the movement on the table choice is between 1 and 9
    # if it's not return a message
    if move >= 1 and move <= 9:
        return True
    else:
        print(" ----------------------------------------")
        print("| Please insert a number between 1 and 9 |")
        print(" ----------------------------------------")
        return False

def valid_number(limit):
    #this function checks if a number is a digit and is between 1 and a limit using other functions
    # if it's not return a message
    while True:
        main_choice = input("Please choose and option: ")
        if is_digit(main_choice):
            if main_is_in_between(main_choice, limit):
                break
    return main_choice

def valid_dif_choice():
    # this function checks if the difficulty choice is a digit and is between 1 and a limit using other functions
    # if it's not return a message
    while True:
        dif_choice = input("     Please choose a difficulty: ")
        if is_digit(dif_choice):
            if dif_is_in_between(dif_choice):
                break
    return dif_choice

def already_taken(Matrix, input):
    #this function checks if a movement is already taken on the table
    if Matrix[(input - 1) // 3][(input - 1) % 3] == " ":
        return True
    else:
        return False

def valid_movement(player, symbol):
    #this function askes the user for a valid movement and only return a value when the value is correct
    #it calls other functions inside and returns the int value of the input
    while True:
        dif_choice = input(f"     PLayer {player}, please choose a movement (number from 1 to 9) for you symbol({symbol}): ")
        if is_digit(dif_choice):
            if movement_is_in_between(int(dif_choice)):
                break
    return int(dif_choice)

def print_certificate(name):
    #this function prints the certificate :))
    print("***************************************************************************************")
    print("*                                                                                     *")
    print("*       Congrats!                                                 Congrats!           *")
    print("*                                                                                     *")
    print("*                       TIC-TAC-TOE  PROFESSIONAL  PLAYER                             *")
    print("*                                                                                     *")
    print("*             Awarded to: {:60s}*".format(name))
    print("*                                                                                     *")
    print("*                                                       *****     *****               *")
    print("*                                                      *     ** **     *              *")
    print("*             Signed by coaches:                        **     *     **               *")
    print("*                    -Vladimir Cuc                       **         **                *")
    print("*                    -Joaquin Janicke                      **     **                  *")
    print("*                                                            ** **                    *")
    print("*                                                              *                      *")
    print("*                                                                                     *")
    print("*                                                                                     *")
    print("*       Congrats!                                                 Congrats!           *")
    print("*                                                                                     *")
    print("*                                                                                     *")
    print("***************************************************************************************")


def history_menu():
    #this function prints the history menu

    print("|------------------------------------------|")
    print("|---------History of Tic Tac Toe-----------|")
    print("|------------------------------------------|")
    print("|             --------------               |")
    print("|            | Menu Options |              |")
    print("|             --------------               |")
    print("|             |1.| Origins                 |")
    print("|             --------------               |")
    print("|             |2.| Evolution               |")
    print("|             --------------               |")
    print("|             |3.| Quit                    |")
    print("|             --------------               |")
    print("|------------------------------------------|")


def origins_menu():
    print("|------------------------------------------|")
    print("|---------Origins of Tic Tac Toe-----------|")
    print("|------------------------------------------|")
    print("|             --------------               |")
    print("|              |  Options |                |")
    print("|             --------------               |")
    print("|             |1.| Romans                  |")
    print("|             --------------               |")
    print("|             |2.| Ancient Egypt           |")
    print("|             --------------               |")
    print("|             |3.| Native Americans        |")
    print("|             --------------               |")
    print("|             |4.| Quit                    |")
    print("|             --------------               |")
    print("|------------------------------------------|")

def print_menu():
    print("|------------------------------------------|")
    print("|---------Welcome To Tic Tac Toe-----------|")
    print("|------------------------------------------|")
    print("|             --------------               |")
    print("|            | Menu Options |              |")
    print("|             --------------               |")
    print("|             |1.| Difficulty              |")
    print("|             --------------               |")
    print("|             |2.| Training                |")
    print("|             --------------               |")
    print("|             |3.| Origin of Tic Tac Toe   |")
    print("|             --------------               |")
    print("|             |4.| Quit                    |")
    print("|             --------------               |")
    print("|------------------------------------------|")

def print_dif_menu():
    print("     |------------------------------------------|")
    print("     |---------------Difficulty Menu------------|")
    print("     |------------------------------------------|")
    print("     |             --------------------         |")
    print("     |            | Difficulty Options |        |")
    print("     |             --------------------         |")
    print("     |             |1.| Easy                    |")
    print("     |             ----------------             |")
    print("     |             |2.| Medium                  |")
    print("     |             ----------------             |")
    print("     |             |3.| Hard                    |")
    print("     |             ----------------             |")
    print("     |             |4.| Multiplayer             |")
    print("     |             ----------------             |")
    print("     |             |5.| Quit                    |")
    print("     |             ----------------             |")
    print("     |------------------------------------------|")

def next_player(user):
    #this function changes the current player to the next player
    if user == 1:
        return 2
    else:
        return 1

def set_pieces(user):
    #this function reads and returns the symbols the player wants to use
    x = input(f"PLayer {user}, insert the symbol you want to play with: ")
    return x

def set_pieces_singlep(symbols):
    #this function reads and returns the symbols the player wants to use and the computer use
    symbols[1] = input("Insert the sybmol you would like to play with: ")
    symbols[2] = input("Insert the sybmol you would like the computer to play with: ")

def move_on_table(user, Matrix, input, symbols):
    #this function changes the space selected with the symbol of the current player
    Matrix[(input-1)//3][(input-1)%3] = symbols[user]

def check_for_win(Matrix):
    #this function checks if the game is over by checking every line of the table
    for i in range (3):
        if Matrix[0][i] == Matrix[1][i] == Matrix[2][i] and Matrix[2][i] != " ":
            return True
        if Matrix[i][0] == Matrix[i][1] == Matrix[i][2] and Matrix[i][0] != " ":
            return True
    if Matrix[0][0] == Matrix[1][1] == Matrix[2][2] and Matrix[0][0] != " ":
        return True
    if Matrix[2][0] == Matrix[1][1] == Matrix[0][2] and Matrix[2][0] != " ":
        return True
    return False

def just_and_enter_idk():
    #this is just a function for an enter to continue, nothing fancy, I didn't have inspiration for a better name :))
    x = input("Please pres enter to continue")

def check_for_tie(Matrix):
    #this function checks for a ties by counting the number of empty spaces left
    nr = 0
    for i in range (3):
        for j in range (3):
            if Matrix[i][j] == " ":
                nr += 1
    if nr == 0:
        return True
    else:
        return False

def pieces_left(Matrix):
    nr = 0
    for i in range(3):
        for j in range(3):
            if Matrix[i][j] == " ":
                nr += 1
    return nr

def computer_easy_move(Matrix, symbols):
    used_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    x = 0
    nr = 0
    while True:
        move = random.randint(1,9)
        ok = 1
        for i in range(9):
            if used_list[i] == move:
                ok = 0
        if ok == 1:
            if already_taken(Matrix, move):
                used_list[nr] = move
                nr += 1
                if pieces_left(Matrix) != 1:

                    if move == 1:
                        if Matrix[((move - 1) // 3)+1][(move - 1) % 3] == Matrix[((move - 1) // 3)+2][(move - 1) % 3] == symbols[1]:
                            used_list[x] = move
                            x+=1
                        elif Matrix[((move - 1) // 3)][((move - 1) % 3)+1] == Matrix[((move - 1) // 3)][((move - 1) % 3)+2] == symbols[1]:
                            used_list[x] = move
                            x += 1
                        elif Matrix[((move - 1) // 3) + 1][((move - 1) % 3)+1] == Matrix[((move - 1) // 3) + 2][((move - 1) % 3)+2] == symbols[1]:
                            used_list[x] = move
                            x += 1
                        else:
                            break
                    elif move == 2:
                        if Matrix[((move - 1) // 3)+1][(move - 1) % 3] == Matrix[((move - 1) // 3)+2][(move - 1) % 3] == symbols[1]:
                            used_list[x] = move
                            x += 1
                        elif Matrix[((move - 1) // 3)][((move - 1) % 3)+1] == Matrix[((move - 1) // 3)][((move - 1) % 3)-1] == symbols[1]:
                            used_list[x] = move
                            x += 1
                        else:
                            break
                    elif move == 3:
                        if Matrix[((move - 1) // 3)+1][(move - 1) % 3] == Matrix[((move - 1) // 3)+2][(move - 1) % 3] == symbols[1]:
                            used_list[x] = move
                            x += 1
                        elif Matrix[((move - 1) // 3)][((move - 1) % 3)-1] == Matrix[((move - 1) // 3)][((move - 1) % 3)-2] == symbols[1]:
                            used_list[x] = move
                            x += 1
                        elif Matrix[((move - 1) // 3) + 1][((move - 1) % 3)-1] == Matrix[((move - 1) // 3) + 2][((move - 1) % 3)-2] == symbols[1]:
                            used_list[x] = move
                            x += 1
                        else:
                            break
                    elif move == 4:
                        if Matrix[((move - 1) // 3)-1][(move - 1) % 3] == Matrix[((move - 1) // 3)+1][(move - 1) % 3] == symbols[1]:
                            used_list[x] = move
                            x += 1
                        elif Matrix[((move - 1) // 3)][((move - 1) % 3)+1] == Matrix[((move - 1) // 3)][((move - 1) % 3)+2] == symbols[1]:
                            used_list[x] = move
                            x += 1
                        else:
                            break
                    elif move == 5:
                        if Matrix[((move - 1) // 3)+1][(move - 1) % 3] == Matrix[((move - 1) // 3)-1][(move - 1) % 3] == symbols[1]:
                            used_list[x] = move
                            x += 1
                        elif Matrix[((move - 1) // 3)][((move - 1) % 3)-1] == Matrix[((move - 1) // 3)][((move - 1) % 3)+1] == symbols[1]:
                            used_list[x] = move
                            x += 1
                        elif Matrix[((move - 1) // 3) + 1][((move - 1) % 3)+1] == Matrix[((move - 1) // 3) - 1][((move - 1) % 3)-1] == symbols[1]:
                            used_list[x] = move
                            x += 1
                        elif Matrix[((move - 1) // 3) - 1][((move - 1) % 3)+1] == Matrix[((move - 1) // 3) + 1][((move - 1) % 3)-1] == symbols[1]:
                            used_list[x] = move
                            x += 1
                        else:
                            break
                    elif move == 6:
                        if Matrix[((move - 1) // 3)-1][(move - 1) % 3] == Matrix[((move - 1) // 3)+1][(move - 1) % 3] == symbols[1]:
                            used_list[x] = move
                            x += 1
                        elif Matrix[((move - 1) // 3)][((move - 1) % 3)-1] == Matrix[((move - 1) // 3)][((move - 1) % 3)-2] == symbols[1]:
                            used_list[x] = move
                            x += 1
                        else:
                            break
                    elif move == 7:
                        if Matrix[((move - 1) // 3)-1][(move - 1) % 3] == Matrix[((move - 1) // 3)-2][(move - 1) % 3] == symbols[1]:
                            used_list[x] = move
                            x += 1
                        elif Matrix[((move - 1) // 3)][((move - 1) % 3)+1] == Matrix[((move - 1) // 3)][((move - 1) % 3)+2] == symbols[1]:
                            used_list[x] = move
                            x += 1
                        elif Matrix[((move - 1) // 3) - 1][((move - 1) % 3)+1] == Matrix[((move - 1) // 3) - 2][((move - 1) % 3)+2] == symbols[1]:
                            used_list[x] = move
                            x += 1
                        else:
                            break
                    elif move == 8:
                        if Matrix[((move - 1) // 3)-1][(move - 1) % 3] == Matrix[((move - 1) // 3)-2][(move - 1) % 3] == symbols[1]:
                            used_list[x] = move
                            x += 1
                        elif Matrix[((move - 1) // 3)][((move - 1) % 3)+1] == Matrix[((move - 1) // 3)][((move - 1) % 3)-1] == symbols[1]:
                            used_list[x] = move
                            x += 1
                        else:
                            break
                    elif move == 9:
                        if Matrix[((move - 1) // 3)-1][(move - 1) % 3] == Matrix[((move - 1) // 3)-2][(move - 1) % 3] == symbols[1]:
                            used_list[x] = move
                            x += 1
                        elif Matrix[((move - 1) // 3)][((move - 1) % 3)-1] == Matrix[((move - 1) // 3)][((move - 1) % 3)-2] == symbols[1]:
                            used_list[x] = move
                            x += 1
                        elif Matrix[((move - 1) // 3) - 1][((move - 1) % 3)-1] == Matrix[((move - 1) // 3) - 2][((move - 1) % 3)-2] == symbols[1]:
                            used_list[x] = move
                            x += 1
                        else:
                            break

                    if pieces_left(Matrix) == x:
                        break
                else:
                    break
    Matrix[(move - 1) // 3][(move - 1) % 3] = symbols[2]

def computer_hard_move(Matrix, symbols):
    okmain = 1
    used_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    x = 0
    nr = 0
    while True:
        move = random.randint(1, 9)

        ok = 1
        for i in range(9):
            if used_list[i] == move:
                ok = 0
        if ok == 1:
            if already_taken(Matrix, move):
                used_list[nr] = move
                nr += 1
                if pieces_left(Matrix) != 1:
                    if move == 1:
                        if Matrix[((move - 1) // 3) + 1][(move - 1) % 3] == Matrix[((move - 1) // 3) + 2][
                            (move - 1) % 3] == \
                                symbols[2]:
                            okmain = 0
                            break
                        elif Matrix[((move - 1) // 3)][((move - 1) % 3) + 1] == Matrix[((move - 1) // 3)][
                            ((move - 1) % 3) + 2] == symbols[2]:
                            okmain = 0
                            break
                        elif Matrix[((move - 1) // 3) + 1][((move - 1) % 3) + 1] == Matrix[((move - 1) // 3) + 2][
                            ((move - 1) % 3) + 2] == symbols[2]:
                            okmain = 0
                            break
                        else:
                            x += 1
                            used_list[x] = move
                    elif move == 2:
                        if Matrix[((move - 1) // 3) + 1][(move - 1) % 3] == Matrix[((move - 1) // 3) + 2][
                            (move - 1) % 3] == \
                                symbols[2]:
                            okmain = 0
                            break
                        elif Matrix[((move - 1) // 3)][((move - 1) % 3) + 1] == Matrix[((move - 1) // 3)][
                            ((move - 1) % 3) - 1] == symbols[2]:
                            okmain = 0
                            break
                        else:
                            x += 1
                            used_list[x] = move
                    elif move == 3:
                        if Matrix[((move - 1) // 3) + 1][(move - 1) % 3] == Matrix[((move - 1) // 3) + 2][
                            (move - 1) % 3] == \
                                symbols[2]:
                            okmain = 0
                            break
                        elif Matrix[((move - 1) // 3)][((move - 1) % 3) - 1] == Matrix[((move - 1) // 3)][
                            ((move - 1) % 3) - 2] == symbols[2]:
                            okmain = 0
                            break
                        elif Matrix[((move - 1) // 3) + 1][((move - 1) % 3) - 1] == Matrix[((move - 1) // 3) + 2][
                            ((move - 1) % 3) - 2] == symbols[2]:
                            okmain = 0
                            break
                        else:
                            x += 1
                            used_list[x] = move
                    elif move == 4:
                        if Matrix[((move - 1) // 3) - 1][(move - 1) % 3] == Matrix[((move - 1) // 3) + 1][
                            (move - 1) % 3] == \
                                symbols[2]:
                            okmain = 0
                            break
                        elif Matrix[((move - 1) // 3)][((move - 1) % 3) + 1] == Matrix[((move - 1) // 3)][
                            ((move - 1) % 3) + 2] == symbols[2]:
                            okmain = 0
                            break
                        else:
                            x += 1
                            used_list[x] = move
                    elif move == 5:
                        if Matrix[((move - 1) // 3) + 1][(move - 1) % 3] == Matrix[((move - 1) // 3) - 1][
                            (move - 1) % 3] == \
                                symbols[2]:
                            okmain = 0
                            break
                        elif Matrix[((move - 1) // 3)][((move - 1) % 3) - 1] == Matrix[((move - 1) // 3)][
                            ((move - 1) % 3) + 1] == symbols[2]:
                            okmain = 0
                            break
                        elif Matrix[((move - 1) // 3) + 1][((move - 1) % 3) + 1] == Matrix[((move - 1) // 3) - 1][
                            ((move - 1) % 3) - 1] == symbols[2]:
                            okmain = 0
                            break
                        elif Matrix[((move - 1) // 3) - 1][((move - 1) % 3) + 1] == Matrix[((move - 1) // 3) + 1][
                            ((move - 1) % 3) - 1] == symbols[2]:
                            okmain = 0
                            break
                        else:
                            x += 1
                            used_list[x] = move

                    elif move == 6:
                        if Matrix[((move - 1) // 3) - 1][(move - 1) % 3] == Matrix[((move - 1) // 3) + 1][
                            (move - 1) % 3] == \
                                symbols[2]:
                            okmain = 0
                            break
                        elif Matrix[((move - 1) // 3)][((move - 1) % 3) - 1] == Matrix[((move - 1) // 3)][
                            ((move - 1) % 3) - 2] == symbols[2]:
                            okmain = 0
                            break
                        else:
                            x += 1
                            used_list[x] = move
                    elif move == 7:
                        if Matrix[((move - 1) // 3) - 1][(move - 1) % 3] == Matrix[((move - 1) // 3) - 2][
                            (move - 1) % 3] == \
                                symbols[2]:
                            okmain = 0
                            break
                        elif Matrix[((move - 1) // 3)][((move - 1) % 3) + 1] == Matrix[((move - 1) // 3)][
                            ((move - 1) % 3) + 2] == symbols[2]:
                            okmain = 0
                            break
                        elif Matrix[((move - 1) // 3) - 1][((move - 1) % 3) + 1] == Matrix[((move - 1) // 3) - 2][
                            ((move - 1) % 3) + 2] == symbols[2]:
                            okmain = 0
                            break
                        else:
                            x += 1
                            used_list[x] = move

                    elif move == 8:
                        if Matrix[((move - 1) // 3) - 1][(move - 1) % 3] == Matrix[((move - 1) // 3) - 2][
                            (move - 1) % 3] == \
                                symbols[2]:
                            okmain = 0
                            break
                        elif Matrix[((move - 1) // 3)][((move - 1) % 3) + 1] == Matrix[((move - 1) // 3)][
                            ((move - 1) % 3) - 1] == symbols[2]:
                            okmain = 0
                            break
                        else:
                            x += 1
                            used_list[x] = move

                    elif move == 9:
                        if Matrix[((move - 1) // 3) - 1][(move - 1) % 3] == Matrix[((move - 1) // 3) - 2][(move - 1) % 3] == symbols[2]:
                            okmain = 0
                            break
                        elif Matrix[((move - 1) // 3)][((move - 1) % 3) - 1] == Matrix[((move - 1) // 3)][
                            ((move - 1) % 3) - 2] == symbols[2]:
                            okmain = 0
                            break
                        elif Matrix[((move - 1) // 3) - 1][((move - 1) % 3) - 1] == Matrix[((move - 1) // 3) - 2][
                            ((move - 1) % 3) - 2] == symbols[2]:
                            okmain = 0
                            break
                        else:
                            x += 1
                            used_list[x] = move

                    if pieces_left(Matrix) == x:
                        break
                else:
                    okmain = 0
                    break
    if okmain == 1:
        used_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        x = 0
        nr = 0
        while True:
            move = random.randint(1, 9)

            ok = 1
            for i in range(9):
                if used_list[i] == move:
                    ok = 0
            if ok == 1:
                if already_taken(Matrix, move):
                    used_list[nr] = move
                    nr += 1
                    if pieces_left(Matrix) != 1:
                        if move == 1:
                            if Matrix[((move - 1) // 3) + 1][(move - 1) % 3] == Matrix[((move - 1) // 3) + 2][
                                (move - 1) % 3] == \
                                    symbols[1]:
                                okmain = 0
                                break
                            elif Matrix[((move - 1) // 3)][((move - 1) % 3) + 1] == Matrix[((move - 1) // 3)][
                                ((move - 1) % 3) + 2] == symbols[1]:
                                okmain = 0
                                break
                            elif Matrix[((move - 1) // 3) + 1][((move - 1) % 3) + 1] == Matrix[((move - 1) // 3) + 2][
                                ((move - 1) % 3) + 2] == symbols[1]:
                                okmain = 0
                                break
                            else:
                                x += 1
                                used_list[x] = move
                        elif move == 2:
                            if Matrix[((move - 1) // 3) + 1][(move - 1) % 3] == Matrix[((move - 1) // 3) + 2][
                                (move - 1) % 3] == \
                                    symbols[1]:
                                okmain = 0
                                break
                            elif Matrix[((move - 1) // 3)][((move - 1) % 3) + 1] == Matrix[((move - 1) // 3)][
                                ((move - 1) % 3) - 1] == symbols[1]:
                                okmain = 0
                                break
                            else:
                                x += 1
                                used_list[x] = move
                        elif move == 3:
                            if Matrix[((move - 1) // 3) + 1][(move - 1) % 3] == Matrix[((move - 1) // 3) + 2][
                                (move - 1) % 3] == \
                                    symbols[1]:
                                okmain = 0
                                break
                            elif Matrix[((move - 1) // 3)][((move - 1) % 3) - 1] == Matrix[((move - 1) // 3)][
                                ((move - 1) % 3) - 2] == symbols[1]:
                                okmain = 0
                                break
                            elif Matrix[((move - 1) // 3) + 1][((move - 1) % 3) - 1] == Matrix[((move - 1) // 3) + 2][
                                ((move - 1) % 3) - 2] == symbols[1]:
                                okmain = 0
                                break
                            else:
                                x += 1
                                used_list[x] = move
                        elif move == 4:
                            if Matrix[((move - 1) // 3) - 1][(move - 1) % 3] == Matrix[((move - 1) // 3) + 1][
                                (move - 1) % 3] == \
                                    symbols[1]:
                                okmain = 0
                                break
                            elif Matrix[((move - 1) // 3)][((move - 1) % 3) + 1] == Matrix[((move - 1) // 3)][
                                ((move - 1) % 3) + 2] == symbols[1]:
                                okmain = 0
                                break
                            else:
                                x += 1
                                used_list[x] = move
                        elif move == 5:
                            if Matrix[((move - 1) // 3) + 1][(move - 1) % 3] == Matrix[((move - 1) // 3) - 1][
                                (move - 1) % 3] == \
                                    symbols[1]:
                                okmain = 0
                                break
                            elif Matrix[((move - 1) // 3)][((move - 1) % 3) - 1] == Matrix[((move - 1) // 3)][
                                ((move - 1) % 3) + 1] == symbols[1]:
                                okmain = 0
                                break
                            elif Matrix[((move - 1) // 3) + 1][((move - 1) % 3) + 1] == Matrix[((move - 1) // 3) - 1][
                                ((move - 1) % 3) - 1] == symbols[1]:
                                okmain = 0
                                break
                            elif Matrix[((move - 1) // 3) - 1][((move - 1) % 3) + 1] == Matrix[((move - 1) // 3) + 1][
                                ((move - 1) % 3) - 1] == symbols[1]:
                                okmain = 0
                                break
                            else:
                                x += 1
                                used_list[x] = move

                        elif move == 6:
                            if Matrix[((move - 1) // 3) - 1][(move - 1) % 3] == Matrix[((move - 1) // 3) + 1][
                                (move - 1) % 3] == \
                                    symbols[1]:
                                okmain = 0
                                break
                            elif Matrix[((move - 1) // 3)][((move - 1) % 3) - 1] == Matrix[((move - 1) // 3)][
                                ((move - 1) % 3) - 2] == symbols[1]:
                                okmain = 0
                                break
                            else:
                                x += 1
                                used_list[x] = move
                        elif move == 7:
                            if Matrix[((move - 1) // 3) - 1][(move - 1) % 3] == Matrix[((move - 1) // 3) - 2][
                                (move - 1) % 3] == \
                                    symbols[1]:
                                okmain = 0
                                break
                            elif Matrix[((move - 1) // 3)][((move - 1) % 3) + 1] == Matrix[((move - 1) // 3)][
                                ((move - 1) % 3) + 2] == symbols[1]:
                                okmain = 0
                                break
                            elif Matrix[((move - 1) // 3) - 1][((move - 1) % 3) + 1] == Matrix[((move - 1) // 3) - 2][
                                ((move - 1) % 3) + 2] == symbols[1]:
                                okmain = 0
                                break
                            else:
                                x += 1
                                used_list[x] = move

                        elif move == 8:
                            if Matrix[((move - 1) // 3) - 1][(move - 1) % 3] == Matrix[((move - 1) // 3) - 2][
                                (move - 1) % 3] == \
                                    symbols[1]:
                                okmain = 0
                                break
                            elif Matrix[((move - 1) // 3)][((move - 1) % 3) + 1] == Matrix[((move - 1) // 3)][
                                ((move - 1) % 3) - 1] == symbols[1]:
                                okmain = 0
                                break
                            else:
                                x += 1
                                used_list[x] = move

                        elif move == 9:
                            if Matrix[((move - 1) // 3) - 1][(move - 1) % 3] == Matrix[((move - 1) // 3) - 2][(move - 1) % 3] == symbols[1]:
                                okmain = 0
                                break
                            elif Matrix[((move - 1) // 3)][((move - 1) % 3) - 1] == Matrix[((move - 1) // 3)][
                                ((move - 1) % 3) - 2] == symbols[1]:
                                okmain = 0
                                break
                            elif Matrix[((move - 1) // 3) - 1][((move - 1) % 3) - 1] == Matrix[((move - 1) // 3) - 2][
                                ((move - 1) % 3) - 2] == symbols[1]:
                                okmain = 0
                                break
                            else:
                                x += 1
                                used_list[x] = move

                        if pieces_left(Matrix) == x:
                            break
                    else:
                        okmain = 0
                        break
    if pieces_left(Matrix) == 9:
        move = 5
        okmain = 0
    if okmain == 1:
        if pieces_left(Matrix) == 8 and check_space(Matrix, 5, symbols[1]) == False:
            move = 5
            okmain = 0
    if okmain == 1:
        if (check_space(Matrix, 5, symbols[2]) and check_space(Matrix, 3, symbols[1]) and check_space(Matrix, 7, symbols[1]) and pieces_left(Matrix) == 6) or\
                (check_space(Matrix, 5, symbols[2]) and check_space(Matrix, 1, symbols[1]) and check_space(Matrix, 9, symbols[1]) and pieces_left(Matrix) == 6):
            x = random.randint(1, 4)
            if x == 1:
                move = 2
                okmain = 0
            elif x == 2:
                move = 4
                okmain = 0
            elif x == 3:
                move = 6
                okmain = 0
            elif x == 4:
                move = 8
                okmain = 0
    if okmain == 1:
        if pieces_left(Matrix) == 6:
            if check_space(Matrix, 5, symbols[2]):
                if Matrix[1][0] == symbols[1] or Matrix[2][0] == symbols[1]:
                    if Matrix[0][1] == symbols[1] or Matrix[0][2] == symbols[1]:
                        move = 1
                        okmain = 0
                if Matrix[0][0] == symbols[1] or Matrix[0][1] == symbols[1]:
                    if Matrix[1][2] == symbols[1] or Matrix[2][2] == symbols[1]:
                        move = 3
                        okmain = 0
                if Matrix[1][0] == symbols[1] or Matrix[0][0] == symbols[1]:
                    if Matrix[2][1] == symbols[1] or Matrix[2][2] == symbols[1]:
                        move = 7
                        okmain = 0
                if Matrix[2][0] == symbols[1] or Matrix[2][1] == symbols[1]:
                    if Matrix[0][2] == symbols[1] or Matrix[1][2] == symbols[1]:
                        move = 9
                        okmain = 0
    if okmain == 1:
        if pieces_left(Matrix) == 7:
            if check_space(Matrix, 5, symbols[2]):
                if check_space(Matrix, 2, symbols[1]):
                    x = random.randint(1, 2)
                    if x == 1:
                        move = 7
                    else:
                        move = 9
                if check_space(Matrix, 6, symbols[1]):
                    x = random.randint(1, 2)
                    if x == 1:
                        move = 7
                    else:
                        move = 1
                if check_space(Matrix, 4, symbols[1]):
                    x = random.randint(1, 2)
                    if x == 1:
                        move = 3
                    else:
                        move = 9
                if check_space(Matrix, 8, symbols[1]):
                    x = random.randint(1, 2)
                    if x == 1:
                        move = 3
                    else:
                        move = 1
    Matrix[(move - 1) // 3][(move - 1) % 3] = symbols[2]

def check_space(Matrix, move, symbol):
    if Matrix[(move - 1) // 3][(move - 1) % 3] == symbol:
        return True
    else:
        return False

def computer_normal_move(Matrix, symbols):
    okmain = 1
    used_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    x = 0
    nr = 0
    while True:
        move = random.randint(1, 9)

        ok = 1
        for i in range(9):
            if used_list[i] == move:
                ok = 0
        if ok == 1:
            if already_taken(Matrix, move):
                used_list[nr] = move
                nr += 1
                if pieces_left(Matrix) != 1:
                    if move == 1:
                        if Matrix[((move - 1) // 3) + 1][(move - 1) % 3] == Matrix[((move - 1) // 3) + 2][
                            (move - 1) % 3] == \
                                symbols[2]:
                            okmain = 0
                            break
                        elif Matrix[((move - 1) // 3)][((move - 1) % 3) + 1] == Matrix[((move - 1) // 3)][
                            ((move - 1) % 3) + 2] == symbols[2]:
                            okmain = 0
                            break
                        elif Matrix[((move - 1) // 3) + 1][((move - 1) % 3) + 1] == Matrix[((move - 1) // 3) + 2][
                            ((move - 1) % 3) + 2] == symbols[2]:
                            okmain = 0
                            break
                        else:
                            x += 1
                            used_list[x] = move
                    elif move == 2:
                        if Matrix[((move - 1) // 3) + 1][(move - 1) % 3] == Matrix[((move - 1) // 3) + 2][
                            (move - 1) % 3] == \
                                symbols[2]:
                            okmain = 0
                            break
                        elif Matrix[((move - 1) // 3)][((move - 1) % 3) + 1] == Matrix[((move - 1) // 3)][
                            ((move - 1) % 3) - 1] == symbols[2]:
                            okmain = 0
                            break
                        else:
                            x += 1
                            used_list[x] = move
                    elif move == 3:
                        if Matrix[((move - 1) // 3) + 1][(move - 1) % 3] == Matrix[((move - 1) // 3) + 2][
                            (move - 1) % 3] == \
                                symbols[2]:
                            okmain = 0
                            break
                        elif Matrix[((move - 1) // 3)][((move - 1) % 3) - 1] == Matrix[((move - 1) // 3)][
                            ((move - 1) % 3) - 2] == symbols[2]:
                            okmain = 0
                            break
                        elif Matrix[((move - 1) // 3) + 1][((move - 1) % 3) - 1] == Matrix[((move - 1) // 3) + 2][
                            ((move - 1) % 3) - 2] == symbols[2]:
                            okmain = 0
                            break
                        else:
                            x += 1
                            used_list[x] = move
                    elif move == 4:
                        if Matrix[((move - 1) // 3) - 1][(move - 1) % 3] == Matrix[((move - 1) // 3) + 1][
                            (move - 1) % 3] == \
                                symbols[2]:
                            okmain = 0
                            break
                        elif Matrix[((move - 1) // 3)][((move - 1) % 3) + 1] == Matrix[((move - 1) // 3)][
                            ((move - 1) % 3) + 2] == symbols[2]:
                            okmain = 0
                            break
                        else:
                            x += 1
                            used_list[x] = move
                    elif move == 5:
                        if Matrix[((move - 1) // 3) + 1][(move - 1) % 3] == Matrix[((move - 1) // 3) - 1][
                            (move - 1) % 3] == \
                                symbols[2]:
                            okmain = 0
                            break
                        elif Matrix[((move - 1) // 3)][((move - 1) % 3) - 1] == Matrix[((move - 1) // 3)][
                            ((move - 1) % 3) + 1] == symbols[2]:
                            okmain = 0
                            break
                        elif Matrix[((move - 1) // 3) + 1][((move - 1) % 3) + 1] == Matrix[((move - 1) // 3) - 1][
                            ((move - 1) % 3) - 1] == symbols[2]:
                            okmain = 0
                            break
                        elif Matrix[((move - 1) // 3) - 1][((move - 1) % 3) + 1] == Matrix[((move - 1) // 3) + 1][
                            ((move - 1) % 3) - 1] == symbols[2]:
                            okmain = 0
                            break
                        else:
                            x += 1
                            used_list[x] = move

                    elif move == 6:
                        if Matrix[((move - 1) // 3) - 1][(move - 1) % 3] == Matrix[((move - 1) // 3) + 1][
                            (move - 1) % 3] == \
                                symbols[2]:
                            okmain = 0
                            break
                        elif Matrix[((move - 1) // 3)][((move - 1) % 3) - 1] == Matrix[((move - 1) // 3)][
                            ((move - 1) % 3) - 2] == symbols[2]:
                            okmain = 0
                            break
                        else:
                            x += 1
                            used_list[x] = move
                    elif move == 7:
                        if Matrix[((move - 1) // 3) - 1][(move - 1) % 3] == Matrix[((move - 1) // 3) - 2][
                            (move - 1) % 3] == \
                                symbols[2]:
                            okmain = 0
                            break
                        elif Matrix[((move - 1) // 3)][((move - 1) % 3) + 1] == Matrix[((move - 1) // 3)][
                            ((move - 1) % 3) + 2] == symbols[2]:
                            okmain = 0
                            break
                        elif Matrix[((move - 1) // 3) - 1][((move - 1) % 3) + 1] == Matrix[((move - 1) // 3) - 2][
                            ((move - 1) % 3) + 2] == symbols[2]:
                            okmain = 0
                            break
                        else:
                            x += 1
                            used_list[x] = move

                    elif move == 8:
                        if Matrix[((move - 1) // 3) - 1][(move - 1) % 3] == Matrix[((move - 1) // 3) - 2][
                            (move - 1) % 3] == \
                                symbols[2]:
                            okmain = 0
                            break
                        elif Matrix[((move - 1) // 3)][((move - 1) % 3) + 1] == Matrix[((move - 1) // 3)][
                            ((move - 1) % 3) - 1] == symbols[2]:
                            okmain = 0
                            break
                        else:
                            x += 1
                            used_list[x] = move

                    elif move == 9:
                        if Matrix[((move - 1) // 3) - 1][(move - 1) % 3] == Matrix[((move - 1) // 3) - 2][(move - 1) % 3] == symbols[2]:
                            okmain = 0
                            break
                        elif Matrix[((move - 1) // 3)][((move - 1) % 3) - 1] == Matrix[((move - 1) // 3)][
                            ((move - 1) % 3) - 2] == symbols[2]:
                            okmain = 0
                            break
                        elif Matrix[((move - 1) // 3) - 1][((move - 1) % 3) - 1] == Matrix[((move - 1) // 3) - 2][
                            ((move - 1) % 3) - 2] == symbols[2]:
                            okmain = 0
                            break
                        else:
                            x += 1
                            used_list[x] = move

                    if pieces_left(Matrix) == x:
                        break
                else:
                    break
    if okmain == 1:
        used_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        x = 0
        nr = 0
        while True:
            move = random.randint(1, 9)

            ok = 1
            for i in range(9):
                if used_list[i] == move:
                    ok = 0
            if ok == 1:
                if already_taken(Matrix, move):
                    used_list[nr] = move
                    nr += 1
                    if pieces_left(Matrix) != 1:
                        if move == 1:
                            if Matrix[((move - 1) // 3) + 1][(move - 1) % 3] == Matrix[((move - 1) // 3) + 2][(move - 1) % 3] == \
                                    symbols[1]:
                                break
                            elif Matrix[((move - 1) // 3)][((move - 1) % 3) + 1] == Matrix[((move - 1) // 3)][
                                ((move - 1) % 3) + 2] == symbols[1]:
                                break
                            elif Matrix[((move - 1) // 3) + 1][((move - 1) % 3) + 1] == Matrix[((move - 1) // 3) + 2][
                                ((move - 1) % 3) + 2] == symbols[1]:
                                break
                            else:
                                x+=1
                                used_list[x] = move
                        elif move == 2:
                            if Matrix[((move - 1) // 3) + 1][(move - 1) % 3] == Matrix[((move - 1) // 3) + 2][(move - 1) % 3] == \
                                    symbols[1]:
                                break
                            elif Matrix[((move - 1) // 3)][((move - 1) % 3) + 1] == Matrix[((move - 1) // 3)][
                                ((move - 1) % 3) - 1] == symbols[1]:
                                break
                            else:
                                x+=1
                                used_list[x] = move
                        elif move == 3:
                            if Matrix[((move - 1) // 3) + 1][(move - 1) % 3] == Matrix[((move - 1) // 3) + 2][(move - 1) % 3] == \
                                    symbols[1]:
                                break
                            elif Matrix[((move - 1) // 3)][((move - 1) % 3) - 1] == Matrix[((move - 1) // 3)][
                                ((move - 1) % 3) - 2] == symbols[1]:
                                break
                            elif Matrix[((move - 1) // 3) + 1][((move - 1) % 3) - 1] == Matrix[((move - 1) // 3) + 2][
                                ((move - 1) % 3) - 2] == symbols[1]:
                                break
                            else:
                                x+=1
                                used_list[x] = move
                        elif move == 4:
                            if Matrix[((move - 1) // 3) - 1][(move - 1) % 3] == Matrix[((move - 1) // 3) + 1][(move - 1) % 3] == \
                                    symbols[1]:
                                break
                            elif Matrix[((move - 1) // 3)][((move - 1) % 3) + 1] == Matrix[((move - 1) // 3)][
                                ((move - 1) % 3) + 2] == symbols[1]:
                                break
                            else:
                                x+=1
                                used_list[x] = move
                        elif move == 5:
                            if Matrix[((move - 1) // 3) + 1][(move - 1) % 3] == Matrix[((move - 1) // 3) - 1][(move - 1) % 3] == \
                                    symbols[1]:
                                break
                            elif Matrix[((move - 1) // 3)][((move - 1) % 3) - 1] == Matrix[((move - 1) // 3)][
                                ((move - 1) % 3) + 1] == symbols[1]:
                                break
                            elif Matrix[((move - 1) // 3) + 1][((move - 1) % 3) + 1] == Matrix[((move - 1) // 3) - 1][
                                ((move - 1) % 3) - 1] == symbols[1]:
                                break
                            elif Matrix[((move - 1) // 3) - 1][((move - 1) % 3) + 1] == Matrix[((move - 1) // 3) + 1][
                                ((move - 1) % 3) - 1] == symbols[1]:
                                break
                            else:
                                x+=1
                                used_list[x] = move

                        elif move == 6:
                            if Matrix[((move - 1) // 3) - 1][(move - 1) % 3] == Matrix[((move - 1) // 3) + 1][(move - 1) % 3] == \
                                    symbols[1]:
                                break
                            elif Matrix[((move - 1) // 3)][((move - 1) % 3) - 1] == Matrix[((move - 1) // 3)][
                                ((move - 1) % 3) - 2] == symbols[1]:
                                break
                            else:
                                x+=1
                                used_list[x] = move
                        elif move == 7:
                            if Matrix[((move - 1) // 3) - 1][(move - 1) % 3] == Matrix[((move - 1) // 3) - 2][(move - 1) % 3] == \
                                    symbols[1]:
                                break
                            elif Matrix[((move - 1) // 3)][((move - 1) % 3) + 1] == Matrix[((move - 1) // 3)][
                                ((move - 1) % 3) + 2] == symbols[1]:
                                break
                            elif Matrix[((move - 1) // 3) - 1][((move - 1) % 3) + 1] == Matrix[((move - 1) // 3) - 2][
                                ((move - 1) % 3) + 2] == symbols[1]:
                                break
                            else:
                                x+=1
                                used_list[x] = move

                        elif move == 8:
                            if Matrix[((move - 1) // 3) - 1][(move - 1) % 3] == Matrix[((move - 1) // 3) - 2][(move - 1) % 3] == \
                                    symbols[1]:
                                break
                            elif Matrix[((move - 1) // 3)][((move - 1) % 3) + 1] == Matrix[((move - 1) // 3)][
                                ((move - 1) % 3) - 1] == symbols[1]:
                                break
                            else:
                                x+=1
                                used_list[x] = move

                        elif move == 9:
                            if Matrix[((move - 1) // 3) - 1][(move - 1) % 3] == Matrix[((move - 1) // 3) - 2][(move - 1) % 3] == symbols[1]:
                                break
                            elif Matrix[((move - 1) // 3)][((move - 1) % 3) - 1] == Matrix[((move - 1) // 3)][((move - 1) % 3) - 2] == symbols[1]:
                                break
                            elif Matrix[((move - 1) // 3) - 1][((move - 1) % 3) - 1] == Matrix[((move - 1) // 3) - 2][((move - 1) % 3) - 2] == symbols[1]:
                                break
                            else:
                                x+=1
                                used_list[x] = move

                        if pieces_left(Matrix) == x:
                            break
                    else:
                        break
    Matrix[(move - 1) // 3][(move - 1) % 3] = symbols[2]

def multiplayer_game(user, symbols):
    win1 = 0
    win2 = 0
    while win1 <2 and win2 <2:
        Matrix = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        print("New Game:")
        print_board(Matrix)
        print(f"Player {user}, you are first")
        while True:
            if user == 1:
                input = valid_movement(user, symbols[1])
            else:
                input = valid_movement(user, symbols[2])
            if already_taken(Matrix, input):
                Matrix[(input - 1) // 3][(input - 1) % 3] = symbols[user]
                print_board(Matrix)
                if check_for_win(Matrix):
                    if user == 1:
                        win1 += 1
                    else:
                        win2 += 1
                    print(f"Player {user}, you won !")
                    print("The score is:")
                    print(f"    Player 1 -> {win1}")
                    print(f"    Player 2 -> {win2}")
                    if win1 == 2 or win2 == 2:
                        print(f"\nCongrats Player {user}, you won the game!\n")
                    just_and_enter_idk()
                    user = next_player(user)
                    break
                elif check_for_tie(Matrix):
                    print("\nIt is a Tie!\n")
                    just_and_enter_idk()
                    user = next_player(user)
                    break
                user = next_player(user)
            else:
                print("\nThis space is already taken, please choose another space\n")

def valid_movement_one():
    while True:
        dif_choice = input(f"     Please choose a movement (number from 1 to 9): ")
        if is_digit(dif_choice):
            if movement_is_in_between(int(dif_choice)) == True:
                break
    return int(dif_choice)

def valid_movement_with_symbol(symbol):
    while True:
        dif_choice = input(f"     Please choose a movement (number from 1 to 9) for you symbol({symbol}): ")
        if is_digit(dif_choice):
            if movement_is_in_between(int(dif_choice)) == True:
                break
    return int(dif_choice)

def game(user, symbols, diff):
    winp = 0
    winc = 0
    while winc < 2 and winp < 2:
        Matrix = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        print("")
        print("New Game:")
        print_board(Matrix)
        if user == 1:
            print("You are first")
        else:
            print("Computer Moves first")
        while True:
            if user == 1:
                input = valid_movement_with_symbol(symbols[1])
                if already_taken(Matrix, input):
                    Matrix[(input - 1) // 3][(input - 1) % 3] = symbols[user]
                    print_board(Matrix)
                    if check_for_win(Matrix):
                        winp += 1
                        print(f"You you won !")
                        print("The score is:")
                        print(f"    Player   -> {winp}")
                        print(f"    Computer -> {winc}")
                        if winp == 2:
                            print(f"\nCongrats you won the game!\n")
                        just_and_enter_idk()
                        user = next_player(user)
                        break
                    elif check_for_tie(Matrix):
                        print("\nIt is a Tie!\n")
                        just_and_enter_idk()
                        user = next_player(user)
                        break
                    user = next_player(user)
                else:
                    print("This space is already taken, please try again!")
            else:
                print(f"    Now the computer will choose a place for his symbol({symbols[2]})")
                just_and_enter_idk()
                if diff == 1:
                    computer_easy_move(Matrix, symbols)
                elif diff == 2:
                    computer_normal_move(Matrix, symbols)
                elif diff == 3:
                    computer_hard_move(Matrix, symbols)
                print_board(Matrix)
                if check_for_win(Matrix):
                    winc += 1
                    print(f"The computer won !")
                    print("The score is:")
                    print(f"    Player   -> {winp}")
                    print(f"    Computer -> {winc}")
                    if winc == 2:
                        print(f"\nThe computer won the game!\n")
                    just_and_enter_idk()
                    user = next_player(user)
                    break
                elif check_for_tie(Matrix):
                    print("\nIt is a Tie!\n")
                    just_and_enter_idk()
                    user = next_player(user)
                    break
                user = next_player(user)

def main():
    while True:
        symbols = ["", "", ""]
        players = [1, 2]
        print_menu()
        main_choice = valid_number(4)
        if main_choice == "1":
            while True:
                print_dif_menu()
                dif_choice = valid_dif_choice()
                if dif_choice == "1":
                    print("Welcome to Easy difficulty Game Mode")
                    print("You will play first to 2 wins against the computer")
                    print("")
                    next_player = random.choice(players)
                    set_pieces_singlep(symbols)
                    game(next_player, symbols, 1)
                elif dif_choice == "2":
                    print("Welcome to Normal difficulty Game Mode")
                    print("You will play first to 2 wins against the computer")
                    print("")
                    next_player = random.choice(players)
                    set_pieces_singlep(symbols)
                    game(next_player, symbols, 2)
                elif dif_choice == '3':
                    print("Welcome to Hard difficulty Game Mode")
                    print("You will play first to 2 wins against the computer")
                    print("")
                    next_player = random.choice(players)
                    set_pieces_singlep(symbols)
                    game(next_player, symbols, 3)
                elif dif_choice == "4":
                    print("Welcome to Multiplayer Game")
                    print("You will play first to 2 wins")

                    next_player = random.choice(players)
                    symbols[1] = set_pieces(1)
                    symbols[2] = set_pieces(2)
                    multiplayer_game(next_player, symbols)

                elif dif_choice == "5":
                    break
        if main_choice == "3":
            while True:
                history_menu()
                choice = valid_number(3)
                if choice == "1":
                    while True:
                        origins_menu()
                        choice2 = valid_number(4)
                        if choice2 == "1":
                            print("Originally played by the Romans as far back as 1300 B.C.")
                            print("and known as Terni Lapilli or \"Three Pebbles at a Time"".")
                            print("Terni Lapilli was played on a circle with 4 lines dividing")
                            print("it into the shape of a cut pizza and as the name states")
                            print("played with three stones. Though the set up is far")
                            print("different from the Tic Tac Toe we have come to know and ")
                            print("love today Terni Lapilli used the same basic logic used")
                            print("in Tic Tac Toe. Rome's Terni Lapilli")
                            print("reflected the logic and set up of common day Tic Tac Toe")
                            just_and_enter_idk()
                        elif choice2 == "2":
                            print(" A similar game was played by the Ancient Egyptians")
                            print("civilizations and Middle Eastern Civilizations as well.")
                            print("Egypt's version of Terni Lapilli was called \"Three Men's\"")
                            print("\"Morris\" with the same board set up as the Roman version")
                            print("with the exception of the board being square instead of")
                            print("circular. In order to win this game, the first player to")
                            print("place all three of their pieces on one of the eight lines")
                            just_and_enter_idk()
                        elif choice2 == "3":
                            print("Three Men's Morris eventually made apperances in China and")
                            print("the Phillipines. Picaria was similar in game play to Three")
                            print("Men's Morris and was played by Native Americans. The 3x3")
                            print("grid that we play on today was developed in the Medieval")
                            print("Times called \"The Magic Square\". ")
                            just_and_enter_idk()
                        else:
                            break
                elif choice == "2":
                    print("Eventually the form of Tic Tac Toe that we know today was")
                    print("developeded in Britain  in the mid 1800s referred to as")
                    print("\"Noughts and Crosses\". Around 1880s Noughts and Crosses ")
                    print("recieves a renaming to \"Tick-Tack-Toe\". Also not")
                    print("suprisingly, the first ever game to be developed on a ")
                    print("computer was tic tac toe, programmed by a Sandy Douglas")
                    print("from England, called OXO. This was the  first time")
                    print("people were able to play against a computer.")
                    just_and_enter_idk()
                else:
                    break
        if main_choice == "2":
            print("")
            print("Welcome to our training!")
            print("")
            name = input("Please enter your name: ")
            print("I will give you 9 scenarios (cause Joaquin likes number 9) and you have to pass all 9 to complete the training")
            print("Good luck")
            print("")
            just_and_enter_idk()
            print("Here is scenario #1")
            print("|---+---+---|   |---+---+---|")
            print("| X |   |   |   | 1 | 2 | 3 |")
            print("|---+---+---|   |---+---+---|")
            print("|   | X | O |   | 4 | 5 | 6 |")
            print("|---+---+---|   |---+---+---|")
            print("| O |   |   |   | 7 | 8 | 9 |")
            print("|---+---+---|   |---+---+---|")
            print("Your are X and the computer is O")
            print("What is the best spot to place your next X?")

            while True:
                user_choice = valid_movement_one()
                if user_choice == 9:
                    print("|---+---+---|   |---+---+---|")
                    print("| X |   |   |   | 1 | 2 | 3 |")
                    print("|---+---+---|   |---+---+---|")
                    print("|   | X | O |   | 4 | 5 | 6 |")
                    print("|---+---+---|   |---+---+---|")
                    print("| O |   | X |   | 7 | 8 | 9 |")
                    print("|---+---+---|   |---+---+---|")
                    print("Great Choice!")
                    just_and_enter_idk()
                    break
                else:
                    print("Oops! Thats not it try again")

            print("Here is scenario #2")
            print("|---+---+---|   |---+---+---|")
            print("| O |   | O |   | 1 | 2 | 3 |")
            print("|---+---+---|   |---+---+---|")
            print("| X | X | O |   | 4 | 5 | 6 |")
            print("|---+---+---|   |---+---+---|")
            print("| O |   | X |   | 7 | 8 | 9 |")
            print("|---+---+---|   |---+---+---|")
            print("Your are X and the computer is O")
            print("What is the best spot to place your next X?")
            while True:
                user_choice = valid_movement_one()
                if user_choice == 2:
                    print("|---+---+---|   |---+---+---|")
                    print("| O | X | O |   | 1 | 2 | 3 |")
                    print("|---+---+---|   |---+---+---|")
                    print("| X | X | O |   | 4 | 5 | 6 |")
                    print("|---+---+---|   |---+---+---|")
                    print("| O |   | X |   | 7 | 8 | 9 |")
                    print("|---+---+---|   |---+---+---|")
                    print("Great Choice!")
                    just_and_enter_idk()
                    break
                else:
                    print("Oops! Thats not it try again")
            print("Here is scenario #3")
            print("|---+---+---|   |---+---+---|")
            print("|   |   |   |   | 1 | 2 | 3 |")
            print("|---+---+---|   |---+---+---|")
            print("| O | X | O |   | 4 | 5 | 6 |")
            print("|---+---+---|   |---+---+---|")
            print("| O |   | X |   | 7 | 8 | 9 |")
            print("|---+---+---|   |---+---+---|")
            print("Your are X and the computer is O")
            print("What is the best spot to place your next X?")

            while True:
                user_choice = valid_movement_one()
                if user_choice == 1:
                    print("|---+---+---|   |---+---+---|")
                    print("| X |   |   |   | 1 | 2 | 3 |")
                    print("|---+---+---|   |---+---+---|")
                    print("| O | X | X |   | 4 | 5 | 6 |")
                    print("|---+---+---|   |---+---+---|")
                    print("| O |   | X |   | 7 | 8 | 9 |")
                    print("|---+---+---|   |---+---+---|")
                    print("Great Choice!")
                    just_and_enter_idk()
                    break
                else:
                    print("Oops! Thats not it try again")

            print("Here is scenario #4")
            print("|---+---+---|   |---+---+---|")
            print("| O |   |   |   | 1 | 2 | 3 |")
            print("|---+---+---|   |---+---+---|")
            print("|   | X | O |   | 4 | 5 | 6 |")
            print("|---+---+---|   |---+---+---|")
            print("| O |   | X |   | 7 | 8 | 9 |")
            print("|---+---+---|   |---+---+---|")
            print("Your are X and the computer is O")
            print("What is the best spot to place your next X?")
            while True:
                user_choice = valid_movement_one()
                if user_choice == 4:
                    print("|---+---+---|   |---+---+---|")
                    print("| O |   |   |   | 1 | 2 | 3 |")
                    print("|---+---+---|   |---+---+---|")
                    print("| X | X | O |   | 4 | 5 | 6 |")
                    print("|---+---+---|   |---+---+---|")
                    print("| O |   | X |   | 7 | 8 | 9 |")
                    print("|---+---+---|   |---+---+---|")
                    print("Great Choice!")
                    just_and_enter_idk()
                    break
                else:
                    print("Oops! Thats not it try again")
            print("Here is scenario #5")
            print("|---+---+---|   |---+---+---|")
            print("| X |   |   |   | 1 | 2 | 3 |")
            print("|---+---+---|   |---+---+---|")
            print("| X | O | O |   | 4 | 5 | 6 |")
            print("|---+---+---|   |---+---+---|")
            print("| O |   |   |   | 7 | 8 | 9 |")
            print("|---+---+---|   |---+---+---|")
            print("Your are X and the computer is O")
            print("What is the best spot to place your next X?")

            while True:
                user_choice = valid_movement_one()
                if user_choice == 3:
                    print("|---+---+---|   |---+---+---|")
                    print("| X |   | X |   | 1 | 2 | 3 |")
                    print("|---+---+---|   |---+---+---|")
                    print("| X | O | O |   | 4 | 5 | 6 |")
                    print("|---+---+---|   |---+---+---|")
                    print("| O |   |   |   | 7 | 8 | 9 |")
                    print("|---+---+---|   |---+---+---|")
                    print("Great Choice!")
                    just_and_enter_idk()
                    break
                else:
                    print("Oops! Thats not it try again")

            print("Here is scenario #6")
            print("|---+---+---|   |---+---+---|")
            print("| O | X | O |   | 1 | 2 | 3 |")
            print("|---+---+---|   |---+---+---|")
            print("| X |   | O |   | 4 | 5 | 6 |")
            print("|---+---+---|   |---+---+---|")
            print("| O |   | X |   | 7 | 8 | 9 |")
            print("|---+---+---|   |---+---+---|")
            print("Your are X and the computer is O")
            print("What is the best spot to place your next X?")
            while True:
                user_choice = valid_movement_one()
                if user_choice == 5:
                    print("|---+---+---|   |---+---+---|")
                    print("| O | X | O |   | 1 | 2 | 3 |")
                    print("|---+---+---|   |---+---+---|")
                    print("| X | X | O |   | 4 | 5 | 6 |")
                    print("|---+---+---|   |---+---+---|")
                    print("| O |   | X |   | 7 | 8 | 9 |")
                    print("|---+---+---|   |---+---+---|")
                    print("Great Choice!")
                    just_and_enter_idk()
                    break
                else:
                    print("Oops! Thats not it try again")
            print("Here is scenario #7")
            print("|---+---+---|   |---+---+---|")
            print("| X | O | X |   | 1 | 2 | 3 |")
            print("|---+---+---|   |---+---+---|")
            print("| X | O | O |   | 4 | 5 | 6 |")
            print("|---+---+---|   |---+---+---|")
            print("| O |   |   |   | 7 | 8 | 9 |")
            print("|---+---+---|   |---+---+---|")
            print("Your are X and the computer is O")
            print("What is the best spot to place your next X?")

            while True:
                user_choice = valid_movement_one()
                if user_choice == 8:
                    print("|---+---+---|   |---+---+---|")
                    print("| X | O | X |   | 1 | 2 | 3 |")
                    print("|---+---+---|   |---+---+---|")
                    print("| X | O | O |   | 4 | 5 | 6 |")
                    print("|---+---+---|   |---+---+---|")
                    print("| O | X |   |   | 7 | 8 | 9 |")
                    print("|---+---+---|   |---+---+---|")
                    print("Great Choice!")
                    just_and_enter_idk()
                    break
                else:
                    print("Oops! Thats not it try again")

            print("Here is scenario #8")
            print("|---+---+---|   |---+---+---|")
            print("| O |   | O |   | 1 | 2 | 3 |")
            print("|---+---+---|   |---+---+---|")
            print("| X | X |   |   | 4 | 5 | 6 |")
            print("|---+---+---|   |---+---+---|")
            print("| O | O | X |   | 7 | 8 | 9 |")
            print("|---+---+---|   |---+---+---|")
            print("Your are X and the computer is O")
            print("What is the best spot to place your next X?")
            while True:
                user_choice = valid_movement_one()
                if user_choice == 6:
                    print("|---+---+---|   |---+---+---|")
                    print("| O |   | O |   | 1 | 2 | 3 |")
                    print("|---+---+---|   |---+---+---|")
                    print("| X | X | X |   | 4 | 5 | 6 |")
                    print("|---+---+---|   |---+---+---|")
                    print("| O | O | X |   | 7 | 8 | 9 |")
                    print("|---+---+---|   |---+---+---|")
                    print("Great Choice!")
                    just_and_enter_idk()
                    break
                else:
                    print("Oops! Thats not it try again")
            print("Here is scenario #9")
            print("|---+---+---|   |---+---+---|")
            print("| X |   | O |   | 1 | 2 | 3 |")
            print("|---+---+---|   |---+---+---|")
            print("|   | O |   |   | 4 | 5 | 6 |")
            print("|---+---+---|   |---+---+---|")
            print("|   |   | X |   | 7 | 8 | 9 |")
            print("|---+---+---|   |---+---+---|")
            print("Your are X and the computer is O")
            print("What is the best spot to place your next X?")

            while True:
                user_choice = valid_movement_one()
                if user_choice == 7:
                    print("|---+---+---|   |---+---+---|")
                    print("| X |   | O |   | 1 | 2 | 3 |")
                    print("|---+---+---|   |---+---+---|")
                    print("|   | O |   |   | 4 | 5 | 6 |")
                    print("|---+---+---|   |---+---+---|")
                    print("| X |   | X |   | 7 | 8 | 9 |")
                    print("|---+---+---|   |---+---+---|")
                    print("Great Choice!")
                    just_and_enter_idk()
                    break
                else:
                    print("Oops! Thats not it try again")
            print("\nCongrats! You passes our training")
            print("You will be awarded with our Tic-Tac-Toe professional certificate!\n")
            just_and_enter_idk()
            print_certificate(name)
            just_and_enter_idk()

        if main_choice == "4":
            print("Thank you for playing, see you soon !")
            break

main()






