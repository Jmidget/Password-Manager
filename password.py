class PassWord:
    import random
    def __init__(self):
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '_', '@', ',']
        self.nwpswrd = ''

	# This function generates a random password(str) of varying length using the characters defined above
    def gen_password(self):
        self.nwpswrd = ''
        pswrd = self.random.sample(self.letters, self.random.randint(2,6)) + self.random.sample(self.numbers, self.random.randint(2,6))  + self.random.sample(self.symbols, self.random.randint(2,6))
        self.random.shuffle(pswrd)
        self.nwpswrd = ''.join(pswrd)