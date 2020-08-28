# Exercise 2: Write another program that prompts for a list of numbers as above and at the end
# prints out both the maximum and minimum of the numbers instead of the average.

total = 0
count = 0
minimum = None
maximum = None
want_data = True

while want_data is True:
    current_number = input("Enter a number: ")
    if current_number == "done":
        want_data = False
        print("Sum:", total, "\nCount:", count, "\nMaximum:", maximum, "\nMinimum:", minimum)
    else:
        try:
            current_number = int(current_number)
        except ValueError as e:
            print("Uh oh, it has to be a number.")
            continue
        total += current_number
        count += 1
        if minimum is None or minimum > current_number:
            minimum = current_number
        if maximum is None or maximum < current_number:
            maximum = current_number
