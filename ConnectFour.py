

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

	def get_win_length(self):
		while True:
			try:
				win_length = int(input("Enter the win length: "))
				if (win_length<= 0 or win_length > self.rows or win_length > self.cols):
					raise ValueError
				return win_length
			except ValueError:
				print("Value entered is not a valid integer.")


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

	def pretty_print_grid(self):
		for row in self.grid:
			print("|",end='')
			for value in row:
				if (value == -1):
					print("R|",end='')
				elif (value == 0):
					print("_|",end='')
				else:
					print("Y|",end='')			
			print()

	def run_loop(self):
		self.rows,self.cols = self.get_grid_size()
		self.win_length = self.get_win_length()
		self.grid = self.create_grid(self.rows,self.cols)
		self.pretty_print_grid()
		return
		while True:
			self.get_user_move()
			self.update_grid()
			self.display_grid()


game = ConnectFour()
game.run_loop()

