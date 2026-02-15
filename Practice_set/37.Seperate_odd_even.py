def odd_num(arr, size):
    odd = []
    for i in range(0, size):
        if arr[i]%2!=0:
            odd.append(arr[i])
    
    return odd
def even_num(arr, size):
    even = []
    for i in range(0, size):
        if arr[i]%2==0:
            even.append(arr[i])
    
    return even

length = int(input("Enter the size of array: "))
num = [0]*length
print("Enter the numebers of array: ")
for n in range(0,length):
    num[n]= int(input("element " +str(n+1)+": "))

print("Odd numbers in the list: "+str(odd_num(num, length)))
print("Even numbers in the list: "+str(even_num(num, length)))