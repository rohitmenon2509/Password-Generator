import random
print('Welcome to Password Generator inc by 2509')
input_letters = int(input("How many letters would you like to have?"))
input_symbols = int(input("And symbols??"))
input_numbers = int(input("Any numbers??"))

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '@', '#', '$', '&', '-', '_']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

raw_password = []
for char in range(1, input_letters + 1):
    raw_password += random.choice(letters)
for char in range(1, input_symbols + 1):
    raw_password += random.choice(numbers)
for char in range(1, input_symbols + 1):
    raw_password += random.choice(symbols)

random.shuffle(raw_password)
password_generated = " "

for char in raw_password:
    password_generated += char
print(password_generated)

