print("CHARU TAMAR 1803010065")
print("Enter length of sides of the triangle: ")
a=int(input("Enter first side:"))
b=int(input("Enter second side:"))
c=int(input("Enter third side:"))
if a==b==c:
    print("Equilateral triangle")
elif a==b or b==c or c==a:
    print("Isosceles triangle")
else:
    print("scalene triangle")
