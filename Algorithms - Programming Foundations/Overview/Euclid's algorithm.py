#GCD is Greatest Common Denominator
#MySolution

def gcd(a,b):
    while (b != 0):
        t = a
        a = b
        b = t%b
    return a

print(gcd(20,8))
print(gcd(60,8))