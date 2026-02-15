def remove_empty_list(arr):
    final = []
    for item in arr:
        if item:
            final.append(item)
    
    return final

a = [[1,2], [], [2], [ ], [1234]]
print(remove_empty_list(a))
length = int(input("Enter the size of array: "))
num = [0]*length
print("Enter the numebers of array: ")
for n in range(0,length):
    num[n]= (input("element " +str(n+1)+": "))

print(remove_empty_list(num))