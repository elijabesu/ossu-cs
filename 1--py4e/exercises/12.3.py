# Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving
# the document from a URL, (2) displaying up to 3000 characters, and (3) counting
# the overall number of characters in the document. Don’t worry about the headers
# for this exercise, simply show the first 3000 characters of the document contents.

import urllib.request, urllib.parse, urllib.error

url = input("Enter - ")
try:
    fhand = urllib.request.urlopen(url)
except:
    print("Invalid url.")
    quit()

numberOfLetters = 0
doc_str = ""
end_str = ""

for line in fhand:
    doc_str += line.decode()

if len(doc_str) < 3000:
    while numberOfLetters < len(doc_str):
        for letter in doc_str:
            numberOfLetters += 1
            end_str += letter
else:
    while numberOfLetters < 3000:
            end_str += doc_str[numberOfLetters]
            numberOfLetters += 1

print(end_str)
print("\nNumber of letters:", len(doc_str))