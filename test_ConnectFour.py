
import unittest
from ConnectFour import ConnectFour

class TestConnectFour(unittest.TestCase):

	def setUp(self):
		self.game = ConnectFour()

	def test_create_grid_correct_shape(self):
		grid = self.game.create_grid(3,4)
		self.assertEqual(len(grid),3)
		self.assertEqual(len(grid[0]),4)

	def test_create_grid_elements_zero(self):
		grid = self.game.create_grid(2,2)
		for row in grid:
			for value in row:
				self.assertEqual(value,0)

	def test_create_grid_reject_non_positive(self):
		with self.assertRaises(ValueError):
			self.game.create_grid(0,6)

	def test_update_grid_correct_position(self):
		game = ConnectFour()
		game.grid = self.game.create_grid(5,5)
		game.rows = 5
		game.turn = -1
		game.update_grid(2)
		self.assertNotEqual(game.grid[4][2],0)



if __name__ == "__main__":
	unittest.main()