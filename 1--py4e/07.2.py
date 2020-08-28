# Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:
# 
# X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point
# number on the line. Count these lines and then compute the total of the spam confidence values from these lines.
# When you reach the end of the file, print out the average spam confidence.
#
# Enter the file name: mbox.txt
# Average spam confidence: 0.894128046745
# 
# Enter the file name: mbox-short.txt
# Average spam confidence: 0.750718518519
# 
# Test your file on the mbox.txt and mbox-short.txt files.

fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except:
    print("File" + fname + "could not be found")
    quit()

count = 0
total = 0
for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        colon_pos = line.find(":")
        number = line[colon_pos+1:]
        number = number.strip()
        number = float(number)
        total += number
        count += 1

print("Average spam confidence:", total / count)