def sec_largest(arr, size):
    if size<2:
        return "list must contain atleast more then two numbers"
    if arr[0]>arr[1]:
        largest = arr[0]
        second = arr[1]
    else:
        largest = arr[1]
        second = arr[0]

    for i in range(2, size):
        if largest < arr[i]:
            second = largest
            largest = arr[i]
    
    return second

length = int(input("Enter the size of array: "))
num = [0]*length
print("Enter the numebers of array: ")
for n in range(0,length):
    num[n]= int(input("element " +str(n+1)+": "))

print("Second Largest number is: "+str(sec_largest(num, length)))