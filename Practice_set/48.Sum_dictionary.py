def sum_dictionary(arr):
    total = 0
    for item in arr:
        total+=int(arr[item])
    return total


p1 ={}
num_entries = int(input("Enter the number of entries: "))

for _ in range(num_entries):
    key = input("Enter key: ")
    value = input("Enter value: ")
    # Add the key-value pair to the dictionary
    p1[key] = value #

print(sum_dictionary(p1))
