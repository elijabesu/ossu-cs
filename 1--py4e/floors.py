floors = input("What floor are you on? ")
try:
    floors = int(floors)
except ValueError as e:
    print("Uh oh, it has to be a number.")
    quit()
us_floors = floors + 1
print("You are on the " + str(us_floors) + "th floor.")