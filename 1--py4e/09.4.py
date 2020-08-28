# Exercise 4: Add code to the above program to figure out who has the most messages
# in the file. After all the data has been read and the dictionary has been created,
# look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum
# loops) to find who has the most messages and print how many messages the person has.
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
    print("File" + fname + "could not be found")
    quit()

emails = list()
emails_count = dict()
for line in fhandle:
    if line.startswith("From "):
        tmp_lst = line.split()
        emails.append(tmp_lst[1])
for email in emails:
    emails_count[email] = emails_count.get(email, 0) + 1

most_emails_address = None
most_emails_count = None
for email,count in emails_count.items():
    if most_emails_count is None or most_emails_count < count:
        most_emails_address = email
        most_emails_count = count
print(most_emails_address, most_emails_count)
