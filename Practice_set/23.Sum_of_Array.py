def sum_array(list):
    sum = 0
    for i in list:
        sum+=i
    return sum

size = int(input("Enter size of Array: "))
num = []
for n in range(0, size):
    num.append(int(input("Enter data: ")))
print("The sum of elements of array: "+str(sum_array(num)))
