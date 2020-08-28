# Exercise 3: Write a program that reads a file and prints
# the letters in decreasing order of frequency. Your program
# should convert all the input to lower case and only count
# the letters a-z. Your program should not count spaces,
# digits, punctuation, or anything other than the letters
# a-z. Find text samples from several different languages
# and see how letter frequency varies between languages.
# Compare your results with the tables at
# https://wikipedia.org/wiki/Letter_frequencies.

import string
PUNCTUATION = string.punctuation

fhandle = open("sources/romeo-punct.txt")

counts = dict()
words = list()
letters = list()

for line in fhandle:
    line = line.rstrip()
    line = line.translate(line.maketrans("", "", PUNCTUATION))
    line = line.lower()
    words += line.split()

for word in words:
    letters += list(word)

for letter in letters:
    counts[letter] = counts.get(letter, 0) + 1

lst = list()

for letter, count in list(counts.items()):
    lst.append((letter, count))

lst.sort()

for letter, count in lst:
    print(letter, count)
