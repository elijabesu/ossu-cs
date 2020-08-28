# Exercise 1: Revise a previous program as follows: Read and parse the “From”
# lines and pull out the addresses from the line. Count the number of messages
# from each person using a dictionary.
# 
# After all the data has been read, print the person with the most commits by
# creating a list of (count, email) tuples from the dictionary. Then sort the
# list in reverse order and print out the person who has the most commits.
# 
# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# 
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
# 
# Enter a file name: mbox.txt
# zqian@umich.edu 195

fname = input("Enter a file name: ")
try:
    fhandle = open(fname)
except:
    print("File " + fname + " could not be found")
    quit()

emails = list()
emails_count = dict()
for line in fhandle:
    if line.startswith("From "):
        tmp_lst = line.split()
        emails.append(tmp_lst[1])
for email in emails:
    emails_count[email] = emails_count.get(email, 0) + 1

lst = list()
for email, count in list(emails_count.items()):
    lst.append((count, email))
lst.sort(reverse = True)

for value, key in lst[:1]:
    print(key, value)
