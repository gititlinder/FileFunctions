#!/usr/bin/python

# Open a file
f = open("foo.txt", "wb")

# Write to a file
f.write( "Python is a great language.\nYeah its great!!\n");
f.close()

# Read from a file
f = open("foo.txt", "r+")

line = f.readline()

while line:
    print line
    line = f.readline()

# Close opened file
f.close()
