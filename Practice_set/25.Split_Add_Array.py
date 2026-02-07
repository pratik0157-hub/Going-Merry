def split_add(list, limit):
    if limit%2!=0:
        return "Array size must be even!!"
    mid = limit//2
    final=[]
    for i in range(0,mid):
        final.append(int(list[i]+list[mid+i]))
    return final
size = int(input("enter the size of Array: "))
num = []
for i in range(0, size):
    num.append(int(input("Enter data: ")))
print("the final array is: ")
print(split_add(num, size))