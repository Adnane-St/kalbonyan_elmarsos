#this is a factorial funtion

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

# def factorial(num):
#     return 1 if num == 0 else num*factorial(num-1)

print("{}! is {}".format(3,factorial(3)))
print("{}! is {}".format(9,factorial(9)))