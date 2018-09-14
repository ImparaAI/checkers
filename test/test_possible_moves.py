import unittest
from checkers.game import Game

class TestPossibleMoves(unittest.TestCase):

	def test_possible_moves(self):
		self.game = Game()

		self.expect([[9, 13], [9, 14], [10, 14], [10, 15], [11, 15], [11, 16], [12, 16]]).move([10, 14])
		self.expect([[21, 17], [22, 17], [22, 18], [23, 18], [23, 19], [24, 19], [24, 20]]).move([23, 18])
		self.expect([[14, 23]]).move([14, 23])
		self.expect([[26, 19], [27, 18]]).move([27, 18])
		self.expect([[6, 10], [7, 10], [9, 13], [9, 14], [11, 15], [11, 16], [12, 16]]).move([9, 13])
		self.expect([[18, 14], [18, 15], [21, 17], [22, 17], [24, 19], [24, 20], [26, 23], [31, 27], [32, 27]]).move([21, 17])
		self.expect([[5, 9], [6, 9], [6, 10], [7, 10], [11, 15], [11, 16], [12, 16]]).move([6, 10])
		self.expect([[17, 14], [18, 14], [18, 15], [24, 19], [24, 20], [25, 21], [26, 23], [31, 27], [32, 27]]).move([18, 14])
		self.expect([[1, 6], [2, 6], [5, 9], [10, 15], [11, 15], [11, 16], [12, 16]]).move([2, 6])
		self.expect([[14, 9], [22, 18], [24, 19], [24, 20], [25, 21], [26, 23], [31, 27], [32, 27]]).move([31, 27])
		self.expect([[5, 9], [6, 9], [10, 15], [11, 15], [11, 16], [12, 16]]).move([11, 16])
		self.expect([[14, 9], [22, 18], [24, 19], [24, 20], [25, 21], [26, 23], [27, 23]]).move([22, 18])
		self.expect([[13, 22]]).move([13, 22])
		self.expect([[22, 31]]).move([22, 31]) #double jump where 10-17 is also in a jumpable position if not for piece restriction
		self.expect([[14, 9], [18, 15], [24, 19], [24, 20], [25, 21], [25, 22], [27, 23], [30, 26]]).move([24, 19])
		self.expect([[10, 17], [16, 23], [31, 24]]).move([31, 24])
		self.expect([[24, 15]]).move([24, 15])
		self.expect([[15, 22]]).move([15, 22])
		self.expect([[25, 18]]).move([25, 18])
		self.expect([[10, 17]]).move([10, 17])
		self.expect([[18, 14], [18, 15], [28, 24], [29, 25], [30, 25], [30, 26], [32, 27]]).move([29, 25])
		self.expect([[5, 9], [6, 9], [6, 10], [7, 10], [7, 11], [8, 11], [16, 19], [16, 20], [17, 21], [17, 22]]).move([17, 21])
		self.expect([[18, 14], [18, 15], [25, 22], [28, 24], [30, 26], [32, 27]]).move([30, 26])
		self.expect([[21, 30]]).move([21, 30])
		self.expect([[18, 14], [18, 15], [26, 22], [26, 23], [28, 24], [32, 27]]).move([18, 15])
		self.expect([[30, 23]]).move([30, 23])
		self.expect([[15, 10], [15, 11], [28, 24], [32, 27]]).move([15, 11])
		self.expect([[8, 15]]).move([8, 15])
		self.expect([[28, 24], [32, 27]]).move([28, 24])
		self.expect([[3, 8], [4, 8], [5, 9], [6, 9], [6, 10], [7, 10], [7, 11], [15, 18], [15, 19], [16, 19], [16, 20], [23, 26], [23, 27], [23, 18], [23, 19]]).move([4, 8])
		self.expect([[24, 19], [24, 20], [32, 27], [32, 28]]).move([24, 19])
		self.expect([[15, 24]]).move([15, 24])
		self.expect([[32, 27], [32, 28]]).move([32, 27])
		self.expect([[23, 32], [24, 31]]).move([23, 32])
		self.expect([])

	def move(self, move):
		self.game.move(move)

	def expect(self, expected_possible_moves):
		self.assertEqual(self.game.get_possible_moves(), expected_possible_moves)
		return self