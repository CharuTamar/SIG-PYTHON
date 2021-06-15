print("CHARU 1803010065")
l1 = input("Enter the elements separated by space:")
l2=l1.split(" ")
with open("write.txt",'w',encoding='utf-8') as f:
    for i in l2:
        f.write('%s ' % i)