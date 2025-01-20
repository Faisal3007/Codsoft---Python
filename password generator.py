import random
lower= ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "y", "u", "v", "w", "x", "y", "z"]
upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "Y", "U", "V", "W", "X", "Y", "Z"]
characters = ["@","#","$","!"]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def suggested_pass(length):
    password = ""
    for _ in range(length):
        # Randomly choose from numbers, lowercase, or uppercase letters
        char_type = random.choice([nums, upper, lower, characters])
        password += str(random.choice(char_type))
    return password

# Generate a 12-character password
pass_len = int(input("Enter length of a password: "))
if pass_len < 8:
	pass_len = int(input("A minimum length of the password must not be less then 8, \n Please enter valid length: "))
	print("Suggested Password:", suggested_pass(pass_len))
else :
	print("Suggested Password:", suggested_pass(pass_len))