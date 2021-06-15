def prod(numbers):
    res = 1
    for n in numbers:
        res *= n
    return res


n1 = int(input("Enter the size of the list: "))
A = list()
print("Enter the elements: ")
for i in range(int(n1)):
    k = int(input(""))
    A.append(k)
print("Result is: ", prod(A))