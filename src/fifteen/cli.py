from math import sqrt
from fifteen import Board, Move, create_random_board, is_solved, make_move


def print_board(board: Board) -> None:
    """Print the board in an ASCII grid format."""
    size = int(sqrt(len(board)))
    cell_width = 2
    horizontal = "+" + ("-" * (cell_width + 2) + "+") * size
    print(horizontal)
    for i in range(size):
        row = board[i * size : (i + 1) * size]
        row_str = ""
        for num in row:
            cell = f"{num:>{cell_width}}" if num != 0 else " " * cell_width
            row_str += f"| {cell} "
        row_str += "|"
        print(row_str)
        print(horizontal)


def main():
    board = create_random_board()
    print("Welcome to the 15-puzzle game!")
    print("Arrange the numbers in order by sliding tiles into the blank space.")
    print("Controls: w = up, a = left, s = down, d = right, n = new game, q = quit")
    print_board(board)
    while not is_solved(board):
        move_input = input("(w/a/s/d/n/q): ").strip().lower()
        move_input = (
            move_input[-1].lower() if move_input else None
        )  # Take only the last character
        match move_input:
            case "w" | "a" | "s" | "d":
                move_map = {
                    "w": Move.UP,
                    "a": Move.LEFT,
                    "s": Move.DOWN,
                    "d": Move.RIGHT,
                }
                try:
                    board = make_move(board, move_map[move_input])
                except ValueError:
                    print("Invalid move. Try again.")
                    print_board(board)
                else:
                    print_board(board)
                    if is_solved(board):
                        print("🎉 Congratulations! You've solved the puzzle!")
                        break
            case "q":
                print("Quitting the game.")
                break
            case "n":
                print("✨ Starting a new game.")
                board = create_random_board()
                print_board(board)
            case _:
                print_board(board)


if __name__ == "__main__":
    main()
