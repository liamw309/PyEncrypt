import keycreater as k
k = k.keycreater()
class encrypt(object):
	'''
	This class is used to actually encrypt the string
	'''
	def __init__(self):
		'''
		This method is used to initialize the class.
		Attributes: initial (what the user wants encrypted), encrypted (the string after it is encrypted).
		'''
		self.initial = []
		self.encrypted = ''
	def getstr(self):
		'''
		This method gets what the user wants to encrypt.
		Attributes: initial (what the user wants encrypted).
		'''
		self.initial = raw_input('What would you like to encrypt? ')
	def encrypter(self):
		'''
		This method takes the string that the user wants encrypted and encrypts it with a for loop.
		Attributes: alphabet (list of characters), key (key), encrypted (encrypted string).
		'''
		alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9']
		key = k.key
		self.encrypted = self.initial.lower()
		for x in range(0,len(alphabet)):
			self.encrypted = self.encrypted.replace(alphabet[x],key[x])

a = encrypt()