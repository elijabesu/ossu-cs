# In this assignment you will read through and parse a file with text and numbers.
# You will extract all the numbers in the file and compute the sum of the numbers.

import re

# sample data:
# fhandle = open("sources/regex_sum_42.txt")

# actual data:
fhandle = open("sources/regex_sum_925874.txt")

matches = list()
for line in fhandle:
    line.rstrip()
    x = re.findall("[0-9]+", line)
    if len(x) > 0:
        for value in x:
            matches.append(int(value))

print(sum(matches))
