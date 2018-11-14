from .board import Board

class Game:

	def __init__(self):
		self.board = Board()
		self.moves = []
		self.consecutive_noncapture_move_limit = 40
		self.moves_since_last_capture = 0

	def move(self, move):
		if move not in self.get_possible_moves():
			raise ValueError('The provided move is not possible')

		self.board = self.board.create_new_board_from_move(move)
		self.moves.append(move)
		self.moves_since_last_capture = 0 if self.board.previous_move_was_capture else self.moves_since_last_capture + 1

		return self

	def move_limit_reached(self):
		return self.moves_since_last_capture >= self.consecutive_noncapture_move_limit

	def is_over(self):
		return self.move_limit_reached() or not self.get_possible_moves()

	def get_winner(self):
		if not self.board.count_movable_player_pieces(1):
			return 2
		elif not self.board.count_movable_player_pieces(2):
			return 1
		else:
			return None

	def get_possible_moves(self):
		return self.board.get_possible_moves()

	def whose_turn(self):
		return self.board.player_turn