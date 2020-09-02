def main():

#    f = open("other/textfile.txt", "w+") # w is for write access, + is for create if file doesn't exist
#    for i in range(10):
#        f.write("This is line " + str(i) + "\n")
#    f.close()

    f = open("other/textfile.txt", "r")
    if f.mode == "r":
        contents = f.read()
        print(contents)

if __name__ == "__main__":
    main()