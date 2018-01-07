# Rooms
import random
import monsters
import player

class Dungeon:
    def __init__(self, name, difficulty, room_no, rooms):
        self.name = name
        self.difficulty = difficulty
        self.room_no = room_no  #Number of rooms
        self.rooms = rooms      #Rooms in dungeon
"""       
    def generate(self):

        for x in range(0, self.room_no):
"""       
    def __str__(self):
        return #Room text of first room. Once room is beaten, move to next room. Print that room text.

potential_shop_items = []
class Shop:
    def __init__(self):
        self.room_text = "A shopkeeper awaits you add the end of the dungeon, eyeing your newfound coin."
        self.sell_items = []    #Items for sale

    def __str__(self):
        return self.room_tex

    def get_sell_items(self):
        item_level = player.lvl #Need to fix player call
        potential_items_same_level = []
        for item in potential_shop_items:
            if item_level:
                item.append(potential_items_same_level)

        for x in range(0,5):
            self.sell_items.append(random.choice(potential_items_same_level))

    def reset_sell_items(self):
        self.sell_items = []

    def print_sell_items(self):
        print("You have " + player().gold + " gold.")   #Tells player what items are for sale.
        for item in self.sell_items:
            print(item)

    def buy_item(self, item):
        for items in sell_items:
            if item == items.name and player.gold <= item.value: # Fix player and item calls. Next 3 lines included.
                player.inventory.append(item)
                self.sell_items -= items
                player.gold -= item.value

available_monsters = [monsters.Skeleton()]
class Room:
	def __init__(self, name, room_text, rating):
		self.name = name
		self.room_text = room_text
		self.rating = rating

	def __str__(self):
		return room_text
    
    def get_monster(self):
        potential_monsters = []
        for mob in available_monsters:
            if mob.rating == self.rating:
                potential_monsters.append(mob)
    mob_in_room = []
    for x in range(0,3):
        mob_in_room.append(random.choice(potential_monsters))

class Begginner_One(Room):          #Temporary
    def __init__(self):
        super().__init__(name = "Begginning Room One", room_text = "First room to the begginning dungeon.", rating = 1)

class Begginner_Dungeon(Dungeon):   #Temporary
    def __init__(self, rooms):
        self.rooms = [Begginner_One()]
        super().__init__(name = "Begginner", rating = 1, noom_no = 1)   