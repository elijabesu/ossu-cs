import os
from os import path
import datetime
from datetime import time
import time

def main():
    print(os.name)

    print("Item exists: " + str(path.exists("other/textfile.txt")))
    print("Item is a file: " + str(path.isfile("other/textfile.txt")))
    print("Item is a directory: " + str(path.isdir("other/textfile.txt")))
    
    print()

    print("Item path: " + str(path.realpath("other/textfile.txt")))
    print("Item path and name: " + str(path.split(path.realpath("other/textfile.txt"))))

    print()

    print(time.ctime(path.getmtime("other/textfile.txt")))
    print(datetime.datetime.fromtimestamp(path.getmtime("other/textfile.txt")))

    print()

    print("It has been " + 
        str(datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("other/textfile.txt"))) + 
        " since the file was modified.")

if __name__ == "__main__":
    main()