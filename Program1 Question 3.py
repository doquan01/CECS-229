class Rectangle:
    def __init__(self, width = 1, height = 1):
        self.width = width
        self.height = height          
        
    def getArea(self):
        return round((self.width * self.height), 2)
    
    def getPerimeter(self):
        return round(((2 * self.width) + (2 * self.height)), 2)

print("Rectangle 1:")
r1 = Rectangle(4,40)
print("Width: " + str(r1.width))
print("Height: " + str(r1.height))
print("Area: " + str(r1.getArea()))
print("Perimeter: " + str(r1.getPerimeter()))

print("\nRectangle 2:")
r2 = Rectangle(3.5,35.9)
print("Width: " + str(r2.width))
print("Height: " + str(r2.height))
print("Area: " + str(r2.getArea()))
print("Perimeter: " + str(r2.getPerimeter()))
