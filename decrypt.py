import keycreater as k
import encrypt as e
k = k.keycreater()
e = e.encrypt()
class decrypt(object):
	'''
	This class is used to decrypt the given string.
	Attrinutes: decrypted (decrypted string).
	'''
	def __init__(self):
		'''
		This method is used to initialized the class.
		Attributes: decrypted (decrypted string).
		'''
		self.decrypted = ''
	def decrypter(self):
		'''
		This method takes in the encrypted string and decrypts it.
		Attributes: alphabet (list of characters), key (key), encrypted (encrypted string), decrypted (decrypted string).
		'''
		alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9']
		encrypted = e.encrypted
		key = k.key
		self.decrypted = encrypted
		for x in range(0,len(alphabet)):
			self.decrypted = self.decrypted.replace(key[x], alphabet[x])
e.getstr()
e.encrypter()
b = decrypt()
b.decrypter()
print(k.key)
print(e.encrypted)
print(b.decrypted)