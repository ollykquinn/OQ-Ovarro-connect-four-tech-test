

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
		if (self.turn == -1):
			print("Red's turn...")
		else:
			print("Yellow's turn...")

		while True:
			try:
				col = int(input("Enter a column number: "))
				if (col<= 0 or col > self.cols or self.grid[0][col-1] != 0):
					raise ValueError
				return col-1
			except ValueError:
				print("Value entered is not a valid column.")

	def update_grid(self,move):
		# March backwards from bottom of grid to find 'dropped' position
		for i in range(self.rows-1,-1,-1):
			if (self.grid[i][move] == 0):
				self.grid[i][move] = self.turn
				return

	def display_grid(self):
		self.pretty_print_grid()

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
		print("|",end='')
		for i in range(self.cols):
			print(str(i+1)+"|",end='')
		print()

	def initialise_game(self):
		self.rows,self.cols = self.get_grid_size()
		self.win_length = self.get_win_length()
		self.grid = self.create_grid(self.rows,self.cols)
		self.turn = -1 # -1=R 1=Y
		self.game_won = False

	def run_loop(self):
		self.display_grid()
		while not self.game_won:
			move = self.get_user_move()
			self.update_grid(move)
			self.display_grid()

			self.turn = self.turn * -1 # Turn alternates between -1 and 1

	def play_game(self):
		self.initialise_game()
		self.run_loop()

if __name__ == "__main__":
	game = ConnectFour()
	game.play_game()

