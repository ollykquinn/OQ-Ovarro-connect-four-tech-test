

class ConnectFour:
	def __init__(self):
		pass

	def init_grid(self,length=7,width=6):
		self.grid = []

	def get_user_move(self):
		pass

	def update_grid(self):
		pass

	def display_grid(self):
		pass

	def run_loop(self):
		while(True):
			self.get_user_move()
			self.update_grid()
			self.display_grid()


game = ConnectFour()
game.run_loop()