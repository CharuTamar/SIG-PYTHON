print("CHARU TAMAR 1803010065")
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
if n1<n2:
    small=n1
else:
    small=n2
for i in range(1,small+1):
    if((n1%i==0) and (n2%i==0)):
        gcd=i
print("GCD is",gcd)
