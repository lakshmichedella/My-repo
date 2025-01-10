#Tic tac toe game with a basic UI

winning_moves = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
player1_moves = []
player2_moves = []
board = [" ", " ", " ", " ", " ", " ", " "," "," "]
moves = []

def printBoard():
        print("", board[0], "|", board[1], "|", board[2])
        print("\n-----------")
        print("", board[3], "|", board[4], "|", board[5])
        print("\n-----------")
        print("", board[6], "|", board[7], "|", board[8])
        print("\n")

def checkWinner():
    for row in winning_moves:
        if all(i in player1_moves for i in row):
            return 1
        elif all(i in player2_moves for i in row):
            return 2
    return 0


print("Tic Tac Toe game")
print("This is a two player game. To place down an X or an O, look at the sample board below and type in the number corresponding to the space")
print("\n The board is contructed like this \n 1 | 2 | 3 \n----------- \n 4 | 5 | 6 \n-----------\n 7 | 8 | 9 ")
print("Let's start the game! \n")
printBoard()

move = 0

#Only 9 squares so only 9 moves
while move < 9:

        try:
                print("Player", str(1 + (move % 2)) + "'s", "move (Denoted by", ["O", "X"][move%2], ")")
                square = int(input("Please type in a number between 1 and 9 (both inclusive): "))
        except:
                #Error testing
                print("Error: Please type in a valid input")
                continue


        if 1 <= square <= 9 and square not in moves:
                board[square-1] = ["O", "X"][move%2]
                move += 1
        else:
                #Error testing
                print("Error: Choose a valid number")
                continue

        moves.append(square)
        printBoard()

        if move % 2:
              player1_moves.append(square)
              player1_moves.sort()
        else:
              player2_moves.append(square)
              player2_moves.sort()

        check = checkWinner()

        if check != 0:
              printBoard()
              print("Winner is Player", check)
              break