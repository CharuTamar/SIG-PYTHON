print("CHARU 1803010065")
n= int(input("Enter the number of lines to read: "))
with open("python.txt",encoding='utf-8') as f:
  for i in range(n):
    print(f.readline())