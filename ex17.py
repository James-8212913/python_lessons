from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying file from {from_file} to {to_file}")

with open (from_file) as in_file, open(to_file, 'w') as outfile:
    in_data = in_file.read()
    outfile.write(in_data)
