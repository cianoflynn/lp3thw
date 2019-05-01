# import argv
from sys import argv
# set the argv list
script, input_file = argv
# print all function
def print_all(f):
    print(f.read())

# move back to start of file 
def rewind(f):
    f.seek(0)

# print the number and line
def print_a_line(line_count, f):
    print(line_count, f.readline(), end = "")

# open the file
current_file = open(input_file)

# message
print("First let's print the whole file:\n")

# call function to print the file
print_all(current_file)

# status message 
print("Now let's rewind, kind of like a tape.")

# call rewind function to move position to 0
rewind(current_file)

# print status message
print("Let's print three lines:")

# set line count to 1
current_line = 1
# print it
print_a_line(current_line, current_file)
# increment
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
