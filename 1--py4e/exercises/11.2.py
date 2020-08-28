# Exercise 2: Write a program to look for lines of the form:
# 
# New Revision: 39772
# 
# Extract the number from each of the lines using a regular
# expression and the findall() method. Compute the average of
# the numbers and print out the average as an integer.
# 
# Enter file:mbox.txt
# 38549
# 
# Enter file:mbox-short.txt
# 39756

import re

fname = input("Enter a file name: ")
try:
    fhandle = open(fname)
except:
    print("File " + fname + " could not be found")
    quit()

matches = list()
for line in fhandle:
    line.rstrip()
    x = re.findall("^New Revision: (\d+)", line)
    if len(x) > 0:
        matches.append(int(x[0]))
print(int(sum(matches) / len(matches)))
