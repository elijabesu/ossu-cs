import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("Enter - ")
html = urllib.request.urlopen(url).read() # read it all into a big string
soup = BeautifulSoup(html, "html.parser") # it will convert it all and you get back an object

# we can then ask it questions, f.e. get all anchor tags as a list
tags = soup("a")
for tag in tags:
    print(tag.get("href", None)) # kinda like a dictionary, href="WE GET THIS"