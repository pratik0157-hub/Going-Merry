def bubble_sort(arr, size):
    if size<2:
        return "list must contain atleast more then two numbers"
    for i in range(0,size):
        for m in range(0,size-1):
            if arr[m]>arr[m+1]:
                dummy = arr[m]
                arr[m] = arr[m+1]
                arr[m+1] = dummy

    return arr

length = int(input("Enter the size of array: "))
num = [0]*length
print("Enter the numebers of array: ")
for n in range(0,length):
    num[n]= int(input("element " +str(n+1)+": ")) 

sorted_list = bubble_sort(num, length)

print("Smallest no: "+str(sorted_list[0]))
print("highest no: "+str(sorted_list[length-1]))