import math
num = 10000

number = []
primes = []

for i in range(num + 1):    #Fills array with numbers to 10000
    number.append(i)

x = 2
while(x < math.sqrt(num)):    
    if (number[x] != 0):       #starts at 2
        a = x * x

        while(a <= num):      #finds multiples of x value and converts it
            number[a] = 0     #to 0
            a = a + x

    x = x + 1      #increment x

for j in range(2,len(number)):
    if(number[j] != 0):          #add remaining numbers that arent 0 to
        primes.append(number[j]) #new array

print(primes)
