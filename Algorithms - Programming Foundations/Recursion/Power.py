#This is a power function

def power(num, pwr):
    if pwr == 0:
        return 1
    else:
        return num * power(num, pwr-1)

print(power(2,10))