# Exercise 5: (Advanced) Change the socket program so that it only shows
# data after the headers and a blank line have been received. Remember
# that recv receives characters (newlines and all), not lines.

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
end_str = ""
numberOfLetters = 0
lookingFor = list("\r\n\r\n")

while True:
    data = mysocket.recv(512)
    if len(data) < 1:
        break
    decoded_data += data.decode()

testing = ""
found = False

while found == False:
    if decoded_data[numberOfLetters] == "\r":
        if decoded_data[numberOfLetters:numberOfLetters + len(lookingFor)] == lookingFor:
            found = True
            numberOfLetters += len(lookingFor)
            end_str += decoded_data[numberOfLetters]
    numberOfLetters += 1
while numberOfLetters < len(decoded_data):
    end_str += decoded_data[numberOfLetters]
    numberOfLetters += 1

print(end_str)

mysocket.close()