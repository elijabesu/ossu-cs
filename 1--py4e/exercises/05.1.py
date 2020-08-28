# Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”.
# Once “done” is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number, detect their mistake using try and except
# and print an error message and skip to the next number.

# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.333333333333333

total = 0
count = 0
want_data = True

while want_data == True:
    current_number = input("Enter a number: ")
    if current_number == "done":
        want_data = False
        print(total, count, total / count)
    else:
        try:
            current_number = float(current_number)
        except ValueError as e:
            print("Uh oh, it has to be a number.")
            continue
        total += current_number
        count += 1
