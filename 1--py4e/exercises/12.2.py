# Exercise 2: Change your socket program so that it counts the number of characters
# it has received and stops displaying any text after it has shown 3000 characters.
# The program should retrieve the entire document and count the total number of
# characters and display the count of the number of characters at the end of the document.

import socket

url = input("Enter - ")
sep_url = url.split("/")

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysocket.connect((sep_url[2], 80))
except:
    print("Invalid url.")
    quit()
cmd = ("GET " + url + " HTTP/1.0\r\n\r\n").encode()
mysocket.send(cmd)

decoded_data = list()
numberOfLetters = 0
end_str = ""

while True:
    data = mysocket.recv(512)
    if len(data) < 1:
        break
    decoded_data += data.decode()

if len(decoded_data) < 3000:
    while numberOfLetters < len(decoded_data):
        for letter in decoded_data:
            numberOfLetters += 1
            end_str += letter
else:
    while numberOfLetters < 3000:
        end_str += decoded_data[numberOfLetters]
        numberOfLetters += 1

print(end_str)
print("\nNumber of letters:", len(decoded_data))

mysocket.close()