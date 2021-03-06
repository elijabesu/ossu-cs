# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create 
# a function called computepay which takes two parameters (hours and rate).

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

def computepay(hours, rate):
    if hours > 40:
        pay = 40 * rate + (hours - 40) * rate * 1.5
    else:
        pay = hours * rate
    return pay

pay = computepay(h, r)
print("Pay: " + str(pay))