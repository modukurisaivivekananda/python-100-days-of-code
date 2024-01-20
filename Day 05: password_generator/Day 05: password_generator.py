print("Welcome to the pypassword generator")
l=input("how many letters would you like in your pasword")
l=int(l)
s=input("how many symbols would you like in your pasword")
s=int(s)
no=input("how many numbers would you like in your pasword")
no=int(no)
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
pwd=[]
for n in range(1,l+1):
    pwd.append(random.choice(letters))
for n in range(1,s+1):
    pwd.append(random.choice(numbers))
for n in range(1,l+1):
    pwd.append(random.choice(symbols))
random.shuffle(pwd)
ct=""
for t in pwd:
    ct=ct+t
print(ct)

