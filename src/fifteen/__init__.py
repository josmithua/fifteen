# fifteen game implementation

from enum import Enum
import random

type Board = tuple[int, ...]
"""A board is represented as a sequence of integers, the blank space represented by 0."""

SIZE = 4

GOAL: Board = tuple(range(1, SIZE * SIZE)) + (0,)
"""Numbers in order with the blank space (0) at the end."""


def is_solved(board: Board) -> bool:
    """Check if the given board is in a solved state."""
    return board == GOAL


def inversions(board: Board) -> int:
    """Count the number of inversions in the board."""
    inv_count = 0
    for i in range(len(board) - 1):
        for j in range(i + 1, len(board)):
            if board[i] and board[j] and board[i] > board[j]:
                inv_count += 1
    return inv_count


def is_solvable(board: Board) -> bool:
    """Check if the given board configuration is solvable."""
    inv = inversions(board)
    blank_pos = board.index(0)
    blank_row_from_bottom = SIZE - (blank_pos // SIZE)

    # If the grid width is odd, return true if inversion count is even.
    if SIZE % 2 == 1:
        return inv % 2 == 0

    if blank_row_from_bottom % 2 == 1:
        return inv % 2 == 0
    else:
        return inv % 2 == 1


def create_random_board() -> Board:
    """Create a new game board in a random state."""
    board = list(GOAL)
    random.shuffle(board)
    while not is_solvable(tuple(board)):
        random.shuffle(board)
    return tuple(board)


class Move(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

    @property
    def opposite(self) -> "Move":
        match self:
            case Move.UP:
                return Move.DOWN
            case Move.DOWN:
                return Move.UP
            case Move.LEFT:
                return Move.RIGHT
            case Move.RIGHT:
                return Move.LEFT


def is_valid_move(board: Board, move: Move) -> bool:
    """Check if the given move is valid. The move is for the piece adjacent to the blank space."""
    # It is easier to check as if we're moving the blank piece, instead of the other piece to the blank space.
    blank_pos = board.index(0)
    blank_space_move = move.opposite
    match blank_space_move:
        case Move.UP:
            return blank_pos >= SIZE
        case Move.DOWN:
            return blank_pos < SIZE * (SIZE - 1)
        case Move.LEFT:
            return blank_pos % SIZE != 0
        case Move.RIGHT:
            return blank_pos % SIZE != SIZE - 1


def make_move(board: Board, move: Move) -> Board:
    """Make the given move on the board and return the new board state."""
    if not is_valid_move(board, move):
        raise ValueError("Invalid move")

    blank_pos = board.index(0)
    target_blank_pos = None
    match move.opposite:
        case Move.UP:
            target_blank_pos = blank_pos - SIZE
        case Move.DOWN:
            target_blank_pos = blank_pos + SIZE
        case Move.LEFT:
            target_blank_pos = blank_pos - 1
        case Move.RIGHT:
            target_blank_pos = blank_pos + 1

    new_board = list(board)
    new_board[blank_pos], new_board[target_blank_pos] = (
        new_board[target_blank_pos],
        new_board[blank_pos],
    )
    return tuple(new_board)
