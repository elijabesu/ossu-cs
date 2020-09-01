import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(("api.saurich.com", 80))
cmd = "GET http://api.saurich.com/hello.txt HTTP/1.0\r\n\r\n".encode()
mysocket.send(cmd)

while True:
    data = mysocket.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end = "")

mysocket.close()

# WE CAN ALSO DO IT BY THIS:
print("\n\nUsing 'urllib':")
# you get no headers but you can ask for them
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen("http://api.saurich.com/hello.txt")
for line in fhand:
    print(line.decode().rstrip())

# we can now work with it like with a normal file
counts = dict()
fhand = urllib.request.urlopen("http://api.saurich.com/hello.txt")
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)