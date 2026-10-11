#Assignment: Tick Tack Toe (X and O)'s

The_Board = {"1": " ", "2": " ", "3": " ", "4": " ", "5": " ", "6": " ", "7": " ", "8": " ", "9": " "}


def print_board(board):
    print(board["1"] + "|" + board["2"] + "|" + board["3"])
    print("-+-+-")
    print(board["4"] + "|" + board["5"] + "|" + board["6"])
    print("-+-+-")
    print(board["7"] + "|" + board["8"] + "|" + board["9"])
    
    
turn = "X"

for i in range(9):
    print_board(The_Board)
    print("Turn for " + turn + ". Move on which space?")
    move = input()
    
    if The_Board[move] == " ":
        The_Board[move] = turn
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
    else:
        print("That space is already occupied. Try again.")
        continue
    
    # Check for a winner
    if (The_Board["1"] == The_Board["2"] == The_Board["3"] != " ") or \
       (The_Board["4"] == The_Board["5"] == The_Board["6"] != " ") or \
       (The_Board["7"] == The_Board["8"] == The_Board["9"] != " ") or \
       (The_Board["1"] == The_Board["4"] == The_Board["7"] != " ") or \
       (The_Board["2"] == The_Board["5"] == The_Board["8"] != " ") or \
       (The_Board["3"] == The_Board["6"] == The_Board["9"] != " ") or \
       (The_Board["1"] == The_Board["5"] == The_Board["9"] != " ") or \
       (The_Board["3"] == The_Board["5"] == The_Board["7"] != " "):
        print_board(The_Board)
        print("Player " + turn + " wins!")
        break


# If space is occupied, ask for input again.
if The_Board[move] == " ":
    The_Board[move] = turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X"