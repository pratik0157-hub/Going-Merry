def arr_multiply(arr, size):
    final = 1
    for i in range(0,size):
        final*= arr[i]
    return final


length = int(input("Enter the size of array: "))
num = [0]*length
print("Enter the numebers of array: ")
for n in range(0,length):
    num[n]= int(input("element " +str(n)+": "))
print("multpication of all elements: "+ str(arr_multiply(num, length)))