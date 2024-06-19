import random
import string
def generate(l):
    characters = string.ascii_letters + string.digits + string.punctuation
    password=[]
    for i in range(l):
        password.append(random.choice(characters))
    return ''.join(password)

print("welcome to the password generator!!")
l=int(input("enter the desired length of your password:"))
password=generate(l)
print("generate password:",password)