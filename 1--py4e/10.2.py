# Exercise 2: This program counts the distribution of the hour
# of the day for each of the messages. You can pull the hour from
# the “From” line by finding the time string and then splitting that
# string into parts using the colon character. Once you have
# accumulated the counts for each hour, print out the counts, one
# per line, sorted by hour as shown below.
# 
# python timeofday.py
# Enter a file name: mbox-short.txt
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1

fname = input("Enter a file name: ")
try:
    fhandle = open(fname)
except:
    print("File " + fname + " could not be found")
    quit()

hours = list()
hours_count = dict()

for line in fhandle:
    if line.startswith("From "):
        hours.append((line.split()[5]).split(":")[0]) 
        # 1. splits the whole line into words
        # 2. takes the 6th word == time
        # 3. splits the time by :
        # 4. takes the 1st part == hour
        # 5. appends the hour to the hours list  

for hour in hours:
    hours_count[hour] = hours_count.get(hour, 0) + 1

tmp = list(hours_count.items())
tmp.sort()
for hour, count in tmp:
    print(hour, count)
