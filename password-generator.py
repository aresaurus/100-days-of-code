#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Order not randomised:
def not_randomised(num_letters, num_symbols, num_numbers):
    password = ''
    for i in range(0, num_letters):
        password += random.choice(letters)
    for i in range(0, num_symbols):
        password += random.choice(symbols)
    for i in range(0, num_numbers):
        password += random.choice(numbers)
    
    return f'Here\'s your password: {password}'

# Order randomised:
def randomised_order(num_letters, num_symbols, num_numbers):
    list_elements = ''
    for i in range(0, num_letters):
        list_elements += random.choice(letters)
    for i in range(0, num_symbols):
        list_elements += random.choice(symbols)
    for i in range(0, num_numbers):
        list_elements += random.choice(numbers)

    password = ''.join(random.sample(list_elements, len(list_elements)))
    return f'Here\'s your password: {password}'


print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

option = int(input('You can choose between having the characters in order (i.e., letters + symbols + numbers) or completely randomised.\nEnter 1 if you prefer the first option, 2 if you prefer the second one.\n'))

while option not in range(1,3):
    option = int(input('Enter a valid value.\n'))
    
if option == 1:
    print(not_randomised(nr_letters, nr_symbols, nr_numbers))
else:
    print(randomised_order(nr_letters, nr_symbols, nr_numbers))
