# Exercise 3: Sometimes when programmers get bored or want to have a bit of fun, they add a harmless
# Easter Egg to their program. Modify the program that prompts the user for the file name so that
# it prints a funny message when the user types in the exact file name “na na boo boo”. The program
# should behave normally for all other files which exist and don’t exist. 

fname = input("Enter a file name: ")
if fname == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    quit()
try:
    fhand = open(fname)
except:
    print("File " + fname + " could not be found")
    quit()

count = 0
total = 0
for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        colon_pos = line.find(":")
        number = line[colon_pos+1:]
        number = number.strip()
        number = float(number)
        total += number
        count += 1

print("Average spam confidence:", total / count)