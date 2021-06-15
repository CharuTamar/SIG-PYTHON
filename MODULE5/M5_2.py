print("CHARU TAMAR 1803010065")
l1 = input("Enter a list of words separated by comma: ")
l2 = l1.split(",")
print(l2)
def longest_word(l2):
    a=[]
    for i in l2:
        a.append(len(i))
    return max(a)
print(longest_word(l2))