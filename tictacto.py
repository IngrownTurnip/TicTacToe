player1mark = ' '
player2mark = ' '
board = [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']
movecount = 0
wincon = False
player1score = 0
player2score = 0
player2movesfirst = False


def printboard():
    print(' | '.join(board[0]))
    print('---------')
    print(' | '.join(board[1]))
    print('---------')
    print(' | '.join(board[2]))
    print(' '.join(' '))


def player_choice():
    choice = 'P'
    global player1mark
    global player2mark
    global player2movesfirst
    while choice != "x" or choice != "o":

        if choice == "x":
            player1mark = 'x'
            player2mark = 'o'
            print("Player one is x, Player 2 is o")
            print(' '.join(' '))
            break
        elif choice == 'o':
            player1mark = 'o'
            player2mark = 'x'
            player2movesfirst = True
            print("Player one is o, Player 2 is x")
            print(' '.join(' '))
            break
        else:
            choice = input("Player 1 choose 'x' or 'o': ")


def player1move():
    print(f"{player1mark}'s turn")
    uinput = '-1'
    uinput2 = ' -1'
    pos = ['0', '1', '2']
    global board
    global movecount
    movenum = 0
    while movenum < 1:

        if uinput in pos:
            movenum += 1
            movecount += 1
            break
        else:
            uinput = input('Row 0-2: ')
    while movenum < 2:

        if uinput2 in pos:
            movenum += 1
            break
        else:
            uinput2 = input('Column 0-2: ')
    if board[int(uinput)][int(uinput2)] == player2mark:
        board[int(uinput)][int(uinput2)] = player2mark
        print(' '.join(' '))
        print('No cheating! Select an unoccupied space!')
        print(' '.join(' '))
        player1move()

    elif board[int(uinput)][int(uinput2)] == player1mark:
        print(' '.join(' '))
        print('You already chose that spot! Select an unoccupied space!')
        print(' '.join(' '))
        player1move()
    else:
        board[int(uinput)][int(uinput2)] = player1mark
        print(' '.join(' '))
        printboard()


def player2move():
    print(f"{player2mark}'s turn")
    uinput = '-1'
    uinput2 = ' -1'
    pos = ['0', '1', '2']
    global board
    global movecount
    movenum = 0
    while movenum < 1:

        if uinput in pos:
            movenum += 1
            movecount += 1
            break
        else:
            uinput = input('Row 0-2: ')
    while movenum < 2:

        if uinput2 in pos:
            movenum += 1
            break
        else:
            uinput2 = input('Column 0-2: ')
    if board[int(uinput)][int(uinput2)] == player1mark:
        board[int(uinput)][int(uinput2)] = player1mark
        print(' '.join(' '))
        print('No cheating! Select an unoccupied space!')
        print(' '.join(' '))
        player2move()

    elif board[int(uinput)][int(uinput2)] == player2mark:
        print(' '.join(' '))
        print('You already chose that spot! Select an unoccupied space!')
        print(' '.join(' '))
        player2move()
    else:
        board[int(uinput)][int(uinput2)] = player2mark
        print(' '.join(' '))
        printboard()


def checkwin():
    global board
    global movecount
    global wincon
    global player1score
    global player2score
    if board[0][0] == 'x' and board[0][1] == 'x' and board[0][2] == 'x':
        wincon = True
        print('X WINS!')
        if player1mark == 'x':
            player1score += 1
        else:
            player2score += 1
    elif board[0][0] == 'x' and board[1][0] == 'x' and board[2][0] == 'x':
        wincon = True
        print('X WINS!')
        if player1mark == 'x':
            player1score += 1
        else:
            player2score += 1
    elif board[1][0] == 'x' and board[1][1] == 'x' and board[1][2] == 'x':
        wincon = True
        print('X WINS!')
        if player1mark == 'x':
            player1score += 1
        else:
            player2score += 1
    elif board[2][0] == 'x' and board[2][1] == 'x' and board[2][2] == 'x':
        wincon = True
        print('X WINS!')
        if player1mark == 'x':
            player1score += 1
        else:
            player2score += 1
    elif board[0][1] == 'x' and board[1][1] == 'x' and board[2][1] == 'x':
        wincon = True
        print('X WINS!')
        if player1mark == 'x':
            player1score += 1
        else:
            player2score += 1
    elif board[0][2] == 'x' and board[1][2] == 'x' and board[2][2] == 'x':
        wincon = True
        print('X WINS!')
        if player1mark == 'x':
            player1score += 1
        else:
            player2score += 1
    elif board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x':
        wincon = True
        print('X WINS!')
        if player1mark == 'x':
            player1score += 1
        else:
            player2score += 1
    elif board[2][0] == 'x' and board[1][1] == 'x' and board[0][2] == 'x':
        wincon = True
        print('X WINS!')
        if player1mark == 'x':
            player1score += 1
        else:
            player2score += 1
    elif board[0][0] == 'o' and board[0][1] == 'o' and board[0][2] == 'o':
        wincon = True
        print('O WINS!')
        if player1mark == 'o':
            player1score += 1
        else:
            player2score += 1
    elif board[0][0] == 'o' and board[1][0] == 'o' and board[2][0] == 'o':
        wincon = True
        print('O WINS!')
        if player1mark == 'o':
            player1score += 1
        else:
            player2score += 1
    elif board[1][0] == 'o' and board[1][1] == 'o' and board[1][2] == 'o':
        wincon = True
        print('O WINS!')
        if player1mark == 'o':
            player1score += 1
        else:
            player2score += 1
    elif board[2][0] == 'o' and board[2][1] == 'o' and board[2][2] == 'o':
        wincon = True
        print('O WINS!')
        if player1mark == 'o':
            player1score += 1
        else:
            player2score += 1
    elif board[0][1] == 'o' and board[1][1] == 'o' and board[2][1] == 'o':
        wincon = True
        print('O WINS!')
        if player1mark == 'o':
            player1score += 1
        else:
            player2score += 1
    elif board[0][2] == 'o' and board[1][2] == 'o' and board[2][2] == 'o':
        wincon = True
        print('O WINS!')
        if player1mark == 'o':
            player1score += 1
        else:
            player2score += 1
    elif board[0][0] == 'o' and board[1][1] == 'o' and board[2][2] == 'o':
        wincon = True
        print('O WINS!')
        if player1mark == 'o':
            player1score += 1
        else:
            player2score += 1
    elif board[2][0] == 'o' and board[1][1] == 'o' and board[0][2] == 'o':
        wincon = True
        print('O WINS!')
        if player1mark == 'o':
            player1score += 1
        else:
            player2score += 1
    elif movecount == 9:
        wincon = True
        print("Tie game!")
    else:
        pass


def gameplay():
    player_choice()
    global player1mark
    global player2mark
    global board
    global movecount
    global wincon
    while wincon == False:
        if player2movesfirst == False:
            checkwin()
            player1move()
            checkwin()

            if wincon == True:
                print(f'Player 1:{player1score}')
                print(f'Player 2:{player2score}')
                ask = input('Would you like a rematch?')
                if ask == 'yes':
                    player1mark = ' '
                    player2mark = ' '
                    board = [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']
                    movecount = 0
                    wincon = False
                    print(' '.join(' '))
                    gameplay()
                else:
                    break
            else:
                pass
            player2move()
            checkwin()
            if wincon == True:
                print(f'Player 1:{player1score}')
                print(f'Player 2:{player2score}')
                ask = input('Would you like a rematch?')
                if ask == 'yes':
                    player1mark = ' '
                    player2mark = ' '
                    board = [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']
                    movecount = 0
                    wincon = False
                    print(' '.join(' '))
                    gameplay()
                else:
                    break
            else:
                pass
        elif player2movesfirst == True:
            checkwin()
            player2move()
            checkwin()

            if wincon == True:
                print(f'Player 1:{player1score}')
                print(f'Player 2:{player2score}')
                ask = input('Would you like a rematch?')
                if ask == 'yes':
                    player1mark = ' '
                    player2mark = ' '
                    board = [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']
                    movecount = 0
                    wincon = False
                    print(' '.join(' '))
                    gameplay()
                else:
                    break
            else:
                player1move()
                checkwin()
                if wincon == True:
                    print(f'Player 1:{player1score}')
                    print(f'Player 2:{player2score}')
                    ask = input('Would you like a rematch?')
                    if ask == 'yes':
                        player1mark = ' '
                        player2mark = ' '
                        board = [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']
                        movecount = 0
                        wincon = False
                        print(' '.join(' '))
                        gameplay()
                    else:
                        break
                else:
                    pass

gameplay()