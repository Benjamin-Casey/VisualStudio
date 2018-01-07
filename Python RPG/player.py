# Player file

class Player:
	def __init__(self):
		self.name = ""
		self.gold = 0
		self.hp = 10
		self.max_hp = 10
		self.weapon = None
		self.dmg = self.weapon
		self.p_class = None
		self.int = 10
		self.str = 10
		self.dex = 10
		self.armor = None
		self.inventory = {}
		self.sate = "menu"	#Defines what the player is currently doing. May change to shopping, combat, etc.
		self.xp = 0
		self.lvl = 1

	def is_alive(self):
		return self.hp >= 0

	def print_inv(self):
		for item in self.inventory:
			print (item)

	def take_dmg(self, dmg):
		self.hp -= dmg

	def lvl_up(self):

		if self.lvl == 1:
			if self.xp >= 100:
				self.lvl += 1
				print("Level up!\nNow level 2!\n")
		elif self.lvl == 2:
			if self.xp >= 400:
				self.lvl += 1
				print("Level up!\nNow level 3!\n")
		elif self.lvl == 3:
			if self.xp >= 1300:
				self.lvl += 1
				print("Level up!\nNow level 4!\n")
		elif self.lvl == 4:
			if self.xp >= 3000:
				self.lvl += 1
				print("Level up!\nNow level 5!\n")

	def move(self):
		pass

