def counter(arr):
    type = {}
    for item in arr:
        if item in type:
            type[item]+=1
        else:
            type[item]=1
    return type

length = int(input("Enter the size of array: "))
num = [0]*length
print("Enter the numebers of array: ")
for n in range(0,length):
    num[n]= (input("element " +str(n+1)+": "))

print(counter(num))
