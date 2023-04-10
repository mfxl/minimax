import unittest
from typing import List
from minimax import find_best_move
from tictactoe import TTTPiece, TTTBoard
from board import Move

class TTTMiniMaxTestCase(unittest.TestCase):
    def test_easy_position(self):
        # Easy to win
        to_win_easy_position: List[TTTPiece] = [TTTPiece.X, TTTPiece.O, TTTPiece.X,
                                                TTTPiece.X, TTTPiece.E, TTTPiece.O,
                                                TTTPiece.E, TTTPiece.E, TTTPiece.O]
        test_board1: TTTBoard = TTTBoard(to_win_easy_position, TTTPiece.X)
        answer1: Move = find_best_move(test_board1)
        self.assertEqual(answer1, 6)
        print("test_board1\n", test_board1)

    def test_block_position(self):
        # Prevent O from winning
        to_block_position: List[TTTPiece] = [TTTPiece.X, TTTPiece.E, TTTPiece.E,
                                             TTTPiece.E, TTTPiece.E, TTTPiece.O,
                                             TTTPiece.E, TTTPiece.X, TTTPiece.O]
        test_board2: TTTBoard = TTTBoard(to_block_position, TTTPiece.X)
        answer2: Move = find_best_move(test_board2)
        print("test_board2\n", test_board2)
        self.assertEqual(answer2, 2)

    def test_hard_position(self):
        # Find best move to win in 2 moves
        to_win_hard_position: List[TTTPiece] = [TTTPiece.X, TTTPiece.E, TTTPiece.E,
                                                TTTPiece.E, TTTPiece.E, TTTPiece.O,
                                                TTTPiece.O, TTTPiece.X, TTTPiece.E]
        test_board3: TTTBoard = TTTBoard(to_win_hard_position, TTTPiece.X)
        answer3: Move = find_best_move(test_board3)
        print("test_board3\n", test_board3)
        self.assertEqual(answer3, 1)
if __name__ == '__main__':
    unittest.main()