def Merging_dictionary(arr1, arr2):
    final = arr1.copy()
    
    for key, value in arr2.items():
        final[key] = value
        
    return final


print("Enter first dictionary data: ")
p1 = {}
num_entries = int(input("Enter the number of entries: "))

for _ in range(num_entries):
    key1 = input("Enter key: ")
    value1 = input("Enter value: ")
    p1[key1] = value1


print("Enter second dictionary data: ")
p2 = {}
num_entries = int(input("Enter the number of entries: "))

for _ in range(num_entries):
    key2 = input("Enter key: ")
    value2 = input("Enter value: ")
    p2[key2] = value2


result = Merging_dictionary(p1, p2)
print("Merged Dictionary:", result)
