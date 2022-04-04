import random

alphabet_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
special_char_list = '!@#$%^&*().,/*-'
num_list = '0123456789'
num = 5
yes = 'y'
no = 'n'

length = input('Enter your desired password length: ')
length = int(length)

num_needed = input('Number required? (y/n)')
num_needed = str(num_needed)

spec_char_needed = input('Special character required? (y/n)')
spec_char_needed = str(spec_char_needed)

print('\nhere is your generated passwords:')

for i in range(num):
    password = ''
    word_length = 0
    if num_needed == yes:
        password += random.choice(num_list)
        word_length += 1
    if spec_char_needed == yes:
        password += random.choice(special_char_list)
        word_length += 1
    for j in range(length-word_length):
        password += random.choice(alphabet_list)
    print(password)
