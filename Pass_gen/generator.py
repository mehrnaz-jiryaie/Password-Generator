from random import sample

# Combined Uppercase and Lowercase Alphabet
characters = [chr(i) for i in range(ord('A'), ord('Z') + 1)] + [chr(i) for i in range(ord('a'), ord('z') + 1)] + [i for i in range(0,10)]

def generate_password(k):
    password_characters = sample(characters, k)
    password = ''.join(str(i) for i in password_characters)
    return password

