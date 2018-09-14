import unittest
from checkers.game import Game

import random

class TestGameOver(unittest.TestCase):

	def setUp(self):
		self.game = Game()

	def test_new_game_not_over(self):
		self.expect(False)

	def test_win_by_capture(self):
		self.make_non_winning_moves([[10, 14], [23, 18], [14, 23], [26, 19], [11, 15], [19, 10], [6, 15], [22, 18], [15, 22], [25, 18], [9, 13], [21, 17], [13, 22],
			[31, 26], [22, 31], [24, 19], [31, 24], [24, 15], [15, 22], [29, 25], [22, 29], [30, 25], [29, 22], [28, 24], [12, 16], [32, 27], [16, 20], [27, 23],
			[20, 27], [23, 18]])

		self.move([22, 15]).expect(True)

	def test_win_by_no_legal_moves(self):
		self.make_non_winning_moves([[11, 15], [22, 18], [15, 22], [25, 18], [12, 16], [18, 14], [9, 18], [23, 14], [10, 17], [21, 14], [5, 9], [14, 5], [6, 9],
			[29, 25], [9, 13], [25, 22], [2, 6], [22, 18], [13, 17], [27, 23], [17, 21], [24, 19], [8, 12], [30, 25], [21, 30], [28, 24], [4, 8], [18, 14], [6, 10],
			[32, 27], [10, 17], [23, 18], [16, 23], [23, 32], [24, 19], [30, 23], [23, 14], [31, 27], [32, 23]])

		self.move([23, 16]).expect(True)

	def test_move_limit_draw(self):
		self.game.move_limit = 15
		self.make_non_winning_moves([[9, 13], [22, 17], [13, 22], [26, 17], [10, 14], [17, 10], [7, 14], [23, 18], [14, 23], [27, 18], [12, 16], [18, 15], [11, 18],
			[25, 22]])

		self.move([18, 25]).expect(True)

	def make_non_winning_moves(self, moves):
		for move in moves:
			self.move(move).expect(False)

	def move(self, move):
		self.game.move(move)
		return self

	def expect(self, value):
		self.assertIs(self.game.is_over(), value)