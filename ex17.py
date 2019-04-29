# imports
from sys import argv
from os.path import exists # boolean check

# arg vars 
script, from_file, to_file = argv

# print out
print(f"Copying for {from_file} to {to_file}")

# we could do these two on one line, how? indata = read(open(fromfile))
in_file = open(from_file)
indata = in_file.read()

#print length of input file.
print(f"The input file is {len(indata)} bytes long")

# use exists function True/False returned.....
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to contine, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

# Close out the open file objects
out_file.close()
in_file.close()
