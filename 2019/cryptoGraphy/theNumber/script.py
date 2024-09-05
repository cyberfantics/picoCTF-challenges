#!/bin/python

alphabat = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
special_chars = '{}\\|/?.,<>!@#$%^&*()_+~`"'
valid_positions = []

def process_position(num):
    if isinstance(num, int) and 1 <= num <= 26:
        valid_positions.append(num)
    elif num in special_chars:
        valid_positions.append(num)

# Taking array of integers as input
input_array = input("Enter an array of integers: ").split()

for item in input_array:
    # Attempt to convert to integer; if not, keep the character as is
    try:
        num = int(item)
        process_position(num)
    except ValueError:
        process_position(item)

# Print the corresponding alphabet for each valid position
for pos in valid_positions:
    if isinstance(pos, int):
        print(alphabat[pos - 1], end='')
    else:
        print(pos, end='')

print()  # Add a newline for better formatting
