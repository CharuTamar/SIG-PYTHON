print("CHARU TAMAR 1803010065")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a>b:
    if b>c:
        print("Median is:",b)
    elif a>c:
        print("Median is:",c)
    else:
        print("Median is:",a)
else:
    if a>c:
        print("Median is:",a)
    elif b>c:
        print("Median is:",c)
    else:
        print("Median is:",b)

