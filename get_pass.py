import random
import string

class PasswordGenerator:
    def __init__(self, length=8):
        self.length = length
        self.password = ""
        
    def generate_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        while True:
            self.password = ''.join(random.choice(characters) for i in range(self.length))
            if (any(char.isdigit() for char in self.password) and
                any(char.isupper() for char in self.password) and
                any(char.islower() for char in self.password) and
                any(char in string.punctuation for char in self.password)):
                break
        
    def get_password(self):
        return self.password
    

password_generator = PasswordGenerator(length=12)
password_generator.generate_password()
password = password_generator.get_password()
print(password)
