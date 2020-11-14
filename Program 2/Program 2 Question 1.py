import random
import math

def isPrime(x):           #check if number is prime
    for i in range(2, math.floor(math.sqrt(x))+1):
        if((x % i) == 0):
            return False
    return True

def euclidAlg(x, y):    #finds the gcd of two numbers
    if (y == 0):        
        return x
    else:
        return euclidAlg(y, (x % y))


p = random.randint(2, 400)       #creates a p and q that is
q = random.randint(2, 400)      #random number between 2 and 400

temp = False                  #generates a prime number for p and
while(temp == False):         #q if it wasnt prime before
    if(isPrime(p) == False and isPrime(q) == False):
        p = random.randint(2,400)
        q = random.randint(2,400)
    elif(isPrime(p) == False):
        p = random.randint(2, 400)
    elif(isPrime(q) == False):
        q = random.randint(2, 400)
    elif(isPrime(p) == True and isPrime(q) == True):
        temp = True

n = p*q                     #Create n part of the key
e = random.randint(2, 400)   #Create e part of the key
gcd = False
while(gcd == False):          #Generate valid e that is prime and is
    eTemp = False               #relatively prime to (p-1)(q-1)
    while(eTemp == False):
        if(isPrime(e) == False):
            e = random.randint(2, 10)
        elif(isPrime(e) == True):
            eTemp = True
    test = (p-1) * (q-1)

    if(euclidAlg(e,test) != 1):
        e = random.randint(2,400)
    elif(euclidAlg(e,test) == 1):
        print("Key(e,n): (", e,", ",n,")")
        gcd = True
        


    





