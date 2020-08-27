# Exercise 7: Rewrite the grade program from the previous chapter using a function 
# called computegrade that takes a score as its parameter and returns a grade as a string.

# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# 
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

score = input("Enter Score: ")
try:
    score = float(score)
except:
    print("Uh oh, it has to be a number.")
    quit()

def computegrade(score):
    if score < 0.0 or score > 1.0:
        return "Uh oh, it has to be between 0 and 1."
    elif score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    else:
        return "F"

grade = computegrade(score)
print(grade)