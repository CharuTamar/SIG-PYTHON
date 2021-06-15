print("CHARU 1803010065")
with open("python.txt",'r',encoding='utf-8') as f:
    count =0
    f1 = f.read()
    lines = f1.split("\n")
    for i in lines:
        count = count+1
    print("Number of lines in a text file are:")
    print(count)
