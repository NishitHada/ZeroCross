import unittest
from board import Board


class TestBoard(unittest.TestCase):

    def test_check_state(self):
        diagonal_case_one = [[1, -1, -1], [0, 1, 0], [0, -1, 1]]
        b1 = Board(diagonal_case_one)
        self.assertEqual(1, b1.check_state(), "Diagonal Test Case 1 Failed!!")

        diagonal_case_two = [[0, -1, 0], [1, 0, -1], [0, 1, 1]]
        b2 = Board(diagonal_case_two)
        self.assertEqual(0, b2.check_state(), "Diagonal Test Case 2 Failed!!")

        tie_case = [[0, 1, 0], [1, 0, 0], [1, 0, 1]]
        b3 = Board(tie_case)
        self.assertEqual(3, b3.check_state(), "Tie Case Failed!!")

        game_rem_case = [[0, 1, 0], [1, 0, 0], [1, 0, -1]]
        b4 = Board(game_rem_case)
        self.assertEqual(2, b4.check_state(), "Game remaining Test Case Failed!!")
