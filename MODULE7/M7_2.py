def checkRange(a,b,n):
    if n in range(a,b):
        print(n, "is in the range of ", a, "and", b)
    else:
        print("The number is outside the range")


a = int(input("Enter the starting index of range: "))
b = int(input("Enter the ending index of range: "))
n = int(input("Enter the number: "))
checkRange(a,b,n)