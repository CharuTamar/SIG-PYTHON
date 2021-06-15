print("CHARU TAMAR 1803010065")
l1 = input("Enter a list of elements separated by comma: ")
l2 = l1.split(",")
print(l2)
for i in range(0,len(l2)):
    if i%2==0:
        l2[i]= "#"
    print(l2[i],end=" ")