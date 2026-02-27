

class ConnectFour:
	def __init__(self):
		pass

	def get_grid_size(self):
		while True:
			try:
				rows = int(input("Enter the number of rows: "))
				if (rows<= 0):
					raise ValueError
				columns = int(input("Enter the number of columns: "))
				if (columns<= 0):
					raise ValueError
				return rows, columns
			except ValueError:
				print("Value entered is not a positive integer.")

	def create_grid(self,rows,cols):
		if (rows <= 0 or cols <= 0):
			raise ValueError("Rows and cols must be positive integers.")
		grid = [[0 for _ in range(cols)] for _ in range(rows)]
		return grid

	def get_user_move(self):
		pass

	def update_grid(self):
		pass

	def display_grid(self):
		pass

	def run_loop(self):
		self.rows,self.cols = self.get_grid_size()
		self.grid = self.init_grid(self.rows,self.cols)
		print(self.grid)
		return
		while True:
			self.get_user_move()
			self.update_grid()
			self.display_grid()


game = ConnectFour()
# game.run_loop()