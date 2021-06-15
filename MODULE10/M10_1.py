class Circle:
    def __init__(self,radius):
        self.radius=radius
    def getArea(self):
        print("Area of circle is:",3.14*self.radius**2)
    def getCircumference(self):
        print("Circumference of circle is:",2*3.14*self.radius)
r= int(input("Enter the value of radius:"))
c= Circle(r)
c.getArea()
c.getCircumference()