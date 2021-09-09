#this is a funcion for countdown

# this is a time libary contains sleep function that we can use to stop our programm for whatever period we want
from time import sleep

def countdown(x):
    if x == 0:
        return print("Done.")
    else:
        print(x)
        sleep(1)
        countdown(x-1)

countdown(10)