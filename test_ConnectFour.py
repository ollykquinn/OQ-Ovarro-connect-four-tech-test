
import unittest
from ConnectFour import ConnectFour

class TestConnectFour(unittest.TestCase):

	def test_create_grid_correct_shape(self):
		game = ConnectFour()
		grid = game.create_grid(3,4)
		self.assertEqual(len(grid),3)
		self.assertEqual(len(grid[0]),4)

	def test_create_grid_elements_zero(self):
		game = ConnectFour()
		grid = game.create_grid(2,2)
		for row in grid:
			for value in row:
				self.assertEqual(value,0)

	def test_create_grid_reject_non_positive(self):
		game = ConnectFour()
		with self.assertRaises(ValueError):
			game.create_grid(0,6)

	def test_update_grid_correct_position(self):
		game = ConnectFour()
		game.grid = game.create_grid(5,5)
		game.rows = 5
		game.turn = -1
		game.update_grid(2)
		self.assertNotEqual(game.grid[4][2],0)

	def test_win_condition_vertical_true(self):
		game = ConnectFour()
		game.win_length = 3
		game.rows=5
		game.cols=5
		game.generate_win_conditions()
		game.grid = game.create_grid(5,5)
		game.grid[4][2] = 1
		game.grid[3][2] = 1
		game.grid[2][2] = 1
		self.assertEqual(game.check_win_condition(),True)

	def test_win_condition_horizontal_true(self):
		game = ConnectFour()
		game.win_length = 3
		game.rows=5
		game.cols=5
		game.generate_win_conditions()
		game.grid = game.create_grid(5,5)
		game.grid[2][4] = 1
		game.grid[2][3] = 1
		game.grid[2][2] = 1
		self.assertEqual(game.check_win_condition(),True)

	def test_win_condition_diagonal_1_true(self):
		game = ConnectFour()
		game.win_length = 3
		game.rows=5
		game.cols=5
		game.generate_win_conditions()
		game.grid = game.create_grid(5,5)
		game.grid[4][4] = 1
		game.grid[3][3] = 1
		game.grid[2][2] = 1
		self.assertEqual(game.check_win_condition(),True)

	def test_win_condition_diagonal_2_true(self):
		game = ConnectFour()
		game.win_length = 3
		game.rows=5
		game.cols=5
		game.generate_win_conditions()
		game.grid = game.create_grid(5,5)
		game.grid[2][4] = 1
		game.grid[3][3] = 1
		game.grid[4][2] = 1
		self.assertEqual(game.check_win_condition(),True)

	def test_win_condition_vertical_false(self):
		game = ConnectFour()
		game.win_length = 3
		game.rows=5
		game.cols=5
		game.generate_win_conditions()
		game.grid = game.create_grid(5,5)
		game.grid[4][2] = 1
		game.grid[3][2] = 0
		game.grid[2][2] = 1
		self.assertEqual(game.check_win_condition(),False)

	def test_win_condition_horizontal_false(self):
		game = ConnectFour()
		game.win_length = 3
		game.rows=5
		game.cols=5
		game.generate_win_conditions()
		game.grid = game.create_grid(5,5)
		game.grid[2][4] = 1
		game.grid[2][3] = 0
		game.grid[2][2] = 1
		self.assertEqual(game.check_win_condition(),False)

	def test_win_condition_diagonal_1_false(self):
		game = ConnectFour()
		game.win_length = 3
		game.rows=5
		game.cols=5
		game.generate_win_conditions()
		game.grid = game.create_grid(5,5)
		game.grid[4][4] = 1
		game.grid[3][3] = 0
		game.grid[2][2] = 1
		self.assertEqual(game.check_win_condition(),False)

	def test_win_condition_diagonal_2_false(self):
		game = ConnectFour()
		game.win_length = 3
		game.rows=5
		game.cols=5
		game.generate_win_conditions()
		game.grid = game.create_grid(5,5)
		game.grid[2][4] = 1
		game.grid[3][3] = 0
		game.grid[4][2] = 1
		self.assertEqual(game.check_win_condition(),False)

	def test_stalemate(self):
		game = ConnectFour()
		game.win_length = 3
		game.rows=3
		game.cols=3
		game.generate_win_conditions()
		game.grid = [[1,-1,-1],
					 [-1,1,1],
					[1,1,-1]]
		self.assertEqual(game.check_win_condition(),False)
		self.assertEqual(game.check_stalemate(),True)


if __name__ == "__main__":
	unittest.main()