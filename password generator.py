import string
import random

length = int(input("password length : "))
lower = string.ascii_lowercase
upper = string.ascii_uppercase
number = string.digits

all = lower + upper + number 

temp = random.sample(all,length)
password = "".join(temp)

print("here ur password")
passwd="".join(random.sample(all,length))

print(password)
