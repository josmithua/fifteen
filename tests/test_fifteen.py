import unittest


from fifteen import is_valid_move, Board, Move, make_move


class TestFifteen(unittest.TestCase):
    def test_is_valid_move(self):
        board: Board = (0, 8, 11, 10, 4, 12, 6, 14, 9, 5, 3, 15, 2, 7, 1, 13)
        self.assertTrue(is_valid_move(board, Move.UP))  # Move 4 up into blank (0)
        self.assertFalse(is_valid_move(board, Move.DOWN))
        self.assertTrue(is_valid_move(board, Move.LEFT))  # Move 8 left into blank (0)
        self.assertFalse(is_valid_move(board, Move.RIGHT))

    def test_make_move(self):
        # Arrange
        board: Board = (0, 8, 11, 10, 4, 12, 6, 14, 9, 5, 3, 15, 2, 7, 1, 13)

        # Act
        new_board = make_move(board, Move.UP)

        # Assert
        expected_board: Board = (4, 8, 11, 10, 0, 12, 6, 14, 9, 5, 3, 15, 2, 7, 1, 13)
        self.assertEqual(new_board, expected_board)


if __name__ == "__main__":
    unittest.main()
