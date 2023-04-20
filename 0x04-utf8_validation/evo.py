#!/usr/bin/python3

S = input("Please, enter a word to count ")
S2 = input("Please, enter a word to be replace ")
file_path = "evolution.txt"  # Replace with the actual file path
with open(file_path, 'r') as file:
        # Read the contents of the file
        file_contents = file.read()
words = file_contents.split()
count = 0

for i in words:
	if S in i:
		count += 1
print(count)
word = file_contents.replace(S, S2)
with open(file_path, 'w') as file:
	if file.write(word):
		print("Successfully replaced")

