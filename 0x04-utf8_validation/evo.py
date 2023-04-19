#!/usr/bin/python3

S = input()
file_path = "evolution.txt"  # Replace with the actual file path
with open(file_path, 'r') as file:
        # Read the contents of the file
        file_contents = file.read()
words = file_contents.split()
count = 0

for i in words:
	if i in S:
		count += 1
print(count)

