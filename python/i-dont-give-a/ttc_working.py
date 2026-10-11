# Assignment: Tick Tack Toe (X and O)

BOARD = {"1": " ", "2": " ", "3": " ", "4": " ", "5": " ", "6": " ", "7": " ", "8": " ", "9": " "}


def print_board(board):
    print(board["1"] + "|" + board["2"] + "|" + board["3"])
    print("-+-+-")
    print(board["4"] + "|" + board["5"] + "|" + board["6"])
    print("-+-+-")
    print(board["7"] + "|" + board["8"] + "|" + board["9"])


def check_winner(board):
    winning_lines = [
        ("1", "2", "3"),
        ("4", "5", "6"),
        ("7", "8", "9"),
        ("1", "4", "7"),
        ("2", "5", "8"),
        ("3", "6", "9"),
        ("1", "5", "9"),
        ("3", "5", "7"),
    ]

    for a, b, c in winning_lines:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]

    return None


def is_valid_move(board, move):
    return move in board and board[move] == " "


def play_game():
    board = BOARD.copy()
    turn = "X"

    while True:
        print_board(board)
        print("Turn for " + turn + ". Move on which space?")
        move = input().strip()

        if not is_valid_move(board, move):
            print("That space is invalid or already occupied. Try again.")
            continue

        board[move] = turn

        winner = check_winner(board)
        if winner:
            print_board(board)
            print("Player " + winner + " wins!")
            break

        if all(space != " " for space in board.values()):
            print_board(board)
            print("It's a draw!")
            break

        turn = "O" if turn == "X" else "X"


if __name__ == "__main__":
    play_game()
