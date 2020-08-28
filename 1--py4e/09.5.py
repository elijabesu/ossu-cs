# Exercise 5: This program records the domain name (instead of the address)
# where the message was sent from instead of who the mail came from (i.e.,
# the whole email address). At the end of the program, print out the contents
# of your dictionary.
# 
# python schoolcount.py
# Enter a file name: mbox-short.txt
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

fname = input("Enter a file name: ")
try:
    fhandle = open(fname)
except:
    print("File" + fname + "could not be found")
    quit()

domains = list()
domains_count = dict()
for line in fhandle:
    if line.startswith("From "):
        words = line.split()
        emails = words[1].split("@")
        domains.append(emails[1])
for domain in domains:
    domains_count[domain] = domains_count.get(domain, 0) + 1
print(domains_count)
