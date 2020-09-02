a = 1
b = 2

def func():
    global b # we are calling for the global variable and changing that one
    b += a

func()
print(b) # prints 3