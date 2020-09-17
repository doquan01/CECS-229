def euclidAlg(x, y):        #Take in two integer input
    if (y == 0):            #base case
        return x
    else:
        return euclidAlg(y, (x % y))    #general case, recursively return y and remainder of (x / y)
a = int(input("Enter one number "))
b = int(input("Enter a second number "))  #Take user inputs and apply inputs to method
print("The greatest common divisor of " + str(a) + " and " + str(b) + " is " + str(euclidAlg(a, b)))
