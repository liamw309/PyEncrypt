import random
class keycreater(object):
    '''
    This class is used to create a key for the encryption
    '''
    def __init__(self):
        '''
        This method helps to create the key. It creates a whole new key by appending a new list (key) and removing it from the old list (alphabet). It does this in a random order.  Attributes: alphabet (base list), key (new list), char (random letter/number from alphabet)
        '''
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.key = []
        while len(self.key) < 35:
        	char = random.choice(alphabet)
	        alphabet.remove(char)
	        self.key.append(char)
    def createkey(self):
        return self.key