def unique_value(d):
    final = []
    for key in d:
        if d[key] not in final:
            final.append(d[key])
    return final

p1 ={}
num_entries = int(input("Enter the number of entries: "))

for _ in range(num_entries):
    key = input("Enter key: ")
    value = input("Enter value: ")
    # Add the key-value pair to the dictionary
    p1[key] = value #

print(unique_value(p1))