class Rectangle:
    def __init__(self, width = 1, height = 1):  #default rectangle of 1 by 1
        self.width = width         #constructor
        self.height = height          
        
    def getArea(self):        #calculate area method
        return round((self.width * self.height), 2)
    
    def getPerimeter(self):   #calculate parimeter method
        return round(((2 * self.width) + (2 * self.height)), 2)

print("Rectangle 1:")    
r1 = Rectangle(4,40)    #construct rectangle of 4 by 40
print("Width: " + str(r1.width))          
print("Height: " + str(r1.height))    #displaying data and calling methods
print("Area: " + str(r1.getArea()))   # of that rectangle
print("Perimeter: " + str(r1.getPerimeter()))

print("\nRectangle 2:")
r2 = Rectangle(3.5,35.9)  #construct rectangle of 3.5 by 35.9
print("Width: " + str(r2.width))
print("Height: " + str(r2.height))      #displaying data and calling methods
print("Area: " + str(r2.getArea()))     # of that rectangle
print("Perimeter: " + str(r2.getPerimeter()))
