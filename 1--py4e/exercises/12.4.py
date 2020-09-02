# Exercise 4: Change the urllinks.py program to extract and count
# paragraph (p) tags from the retrieved HTML document and display
# the count of the paragraphs as the output of your program. Do not
# display the paragraph text, only count them. Test your program on
# several small web pages as well as some larger web pages.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
try:
    html = urlopen(url, context=ctx).read()
except:
    print("Invalid url.")
    quit()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('p')
#numberOfTags = 0
#for tag in tags:
#    numberOfTags += 1
#print("Number of paragraphs:", numberOfTags)

#for numberOfTags, tag in enumerate(tags):
#    continue
#print("Number of paragraphs:", (numberOfTags + 1))

print("Number of paragraphs:", len(tags))