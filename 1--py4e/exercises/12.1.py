# Exercise 1: Change the socket program socket1.py to prompt the user for the URL so it can read any web page.
# You can use split('/') to break the URL into its component parts so you can extract the host name for the
# socket connect call. Add error checking using try and except to handle the condition where the user enters
# an improperly formatted or non-existent URL.

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

while True:
    data = mysocket.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end = "")

mysocket.close()