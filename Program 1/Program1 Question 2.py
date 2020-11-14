def convert(x):
    x = int(x)
    decimal = 0
    power = 1
    while (x>0):
        last = x % 10
        x = int(x / 10)
        decimal += (last * power)
        power = power * 2
    return decimal
        
binary = input("Enter a binary string\n") #take in user input

print(convert (binary)) #convert binary string into decimal using method
print(int (binary,2)) #convert binary string into base 10 integer with inbuilt int
