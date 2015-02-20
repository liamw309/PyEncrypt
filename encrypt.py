import keycreater as k
k = k.keycreater()
print(k.key)
class encrypt(object):
	'''
	This class is used to actually encrypt the string
	'''
	def __init__(self):
		self.initial = []
		self.new = ''
	def getstr(self):
		self.initial = raw_input('What would you like to encrypt? ')
	def encrypt(self):
		alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9']
		key = k.key
		self.new = self.initial.lower()
		for x in range(0,35):
			self.new.replace(alphabet[x],key[x])
	def getencrypt(self):
		return self.new, self.initial

a = encrypt()
a.getstr()
a.encrypt()
a.getencrypt()
print(a.new)