# Items

class Item:
	def __init__(self, name, value, rating):
		self.name = name		#Item name
		self.description = description #Item Description
		self.value = value		#Gold value of item
		self.rating = rating	#Rating of item. Better items (higher rating) are found later in the campaign.

class Weapon(Item):
	def __init__(self, damage):
		super().__init__(name, value, rating)
		self.damage = damage

	def __str__(self):
		return "{}\n{}\nDamage: {}\n Value: {}".format(self.name, self.description, self.damage, self.value)

class Gold:
	def __init__(self):
		self.name = "Gold"
		self.description = "A glistening coin of gold."

	def __str__(self):
		return "{}\n{}\n".format(self.name, self.description)
