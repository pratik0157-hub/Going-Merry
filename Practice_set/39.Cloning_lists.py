def clone(arr):
    clone1 = []
    for item in arr:
        if item:
            clone1.append(item)
    return clone1
length = int(input("Enter the size of array: "))
num = [0]*length
print("Enter the numebers of array: ")
for n in range(0,length):
    num[n]= int(input("element " +str(n+1)+": "))
clone2 = clone(num)
clone2[0] = 10
print(clone2[0])
print(num[0])