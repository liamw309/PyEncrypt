import random
key = []
class keycreater:
	def createkey(self):
		global key
		'''
		This method helps to create the key. It creates a whole new key by appending a
		new list (key) and removing it from the old list (alphabet). It does this in a random order.

		Attributes: alphabet (base list), key (new list), char (random letter/number from alphabet)
		'''
		alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9']
		key = []
		while len(key) < 35:
			char = random.choice(alphabet)
			alphabet.remove(char)
			key.append(char)
		return key