

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

	# If the top row is full (and no one has already won) then no one will win
	def check_stalemate(self):
		total = 0
		topRow = self.grid[0]
		for i in range(self.cols):
			total += abs(topRow[i])
		if (total == self.cols):
			return True
		return False

	# Generates kernels used to detect wins
	def generate_win_conditions(self):
		self.vertical = [[1] for _ in range(self.win_length)]
		self.horizontal = [[1 for _ in range(self.win_length)]]
		self.diagonal_1 = [[0 for _ in range(self.win_length)] for _ in range(self.win_length)]
		self.diagonal_2 = [[0 for _ in range(self.win_length)] for _ in range(self.win_length)]
		for i in range(self.win_length):
			self.diagonal_1[i][i] = 1
			self.diagonal_2[self.win_length-i-1][i] = 1

	def check_win_condition(self):
		if self.convolve(self.vertical) != 0:
			return True
		if self.convolve(self.horizontal) != 0:
			return True
		if self.convolve(self.diagonal_1) != 0:
			return True
		if self.convolve(self.diagonal_2) != 0:
			return True
		return False


	# Treating the grid as an image winning alignments can be detected by performing convolutions with kernels containing the winning 'pattern' (i.e. n in a row/column/diagonal) 
	# This works by tallying up the values in local stretches of the grid, if the tally reaches the win_length a winning row/column/diagonal has been found
	def convolve(self, kernel):
		kernel_height = len(kernel)
		kernel_width = len(kernel[0])

		center_y = kernel_height // 2
		center_x = kernel_width // 2

		for i in range(self.rows):
			for j in range(self.cols):
				acc = 0 
				for m in range(kernel_height):
					for n in range(kernel_width):
						y = i + m - center_y
						x = j + n - center_x
						if 0 <= y < self.rows and 0 <= x < self.cols:
							acc += self.grid[y][x] * kernel[m][n]
				if acc == self.win_length:
					return 1
				if acc == -self.win_length:
					return -1
		return 0


	def initialise_game(self):
		self.rows,self.cols = self.get_grid_size()
		self.win_length = self.get_win_length()
		self.generate_win_conditions()
		self.grid = self.create_grid(self.rows,self.cols)
		self.turn = -1 # -1=R 1=Y

	def run_loop(self):
		self.display_grid()
		while True:
			move = self.get_user_move()
			self.update_grid(move)
			self.display_grid()
			if self.check_win_condition():
				return
			if self.check_stalemate():
				self.turn = 0
				return
			self.turn = self.turn * -1 # Turn alternates between -1 and 1 - set to 0 if stalemate
		

	def play_game(self):
		self.initialise_game()
		self.run_loop()
		if (self.turn == -1):
			print("Red wins!")
		elif (self.turn == 1):
			print("Yellow wins!")
		else:
			print("It's a draw!")

if __name__ == "__main__":
	game = ConnectFour()
	game.play_game()

