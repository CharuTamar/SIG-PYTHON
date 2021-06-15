print("CHARU 1803010065")
with open("python.txt",mode='a',encoding='utf-8') as f:
    f.write("This is appended line")
appended_file = open("python.txt",'r')
print(appended_file.read())
