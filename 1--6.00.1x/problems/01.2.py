# Assume s is a string of lower case characters.
# 
# Write a program that prints the number of times the string
# 'bob' occurs in s. For example, if s = 'azcbobobegghakl',
# then your program should print
# 
# Number of times bob occurs is: 2

s = 'azcbobobegghakl'
lookingFor = 'bob'
bobCount1 = 0
bobCount2 = 0

for i in range(len(s)):
    if s[i:i + len(lookingFor)] == lookingFor:
        bobCount1 += 1
print("Number of times bob occurs is:", bobCount1)


for i, l in enumerate(s):
    if s[i:i + len(lookingFor)] == lookingFor:
        bobCount2 += 1
print("Number of times bob occurs is:", bobCount2)