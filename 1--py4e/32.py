# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

hrs = input("Enter Hours: ")
try:
    h = float(hrs)
except ValueError as e:
    print("Uh oh, it has to be a number.")
    quit()

rate = input("Enter Rate: ")
try:
    r = float(rate)
except ValueError as e:
    print("Uh oh, it has to be a number.")
    quit()

if h > 40:
    pay = 40 * r + (h - 40) * r * 1.5
else:
    pay = h * r

print("Pay: " + str(pay))