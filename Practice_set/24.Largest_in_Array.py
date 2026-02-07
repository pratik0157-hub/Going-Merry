def largest_element(list, limit):
    check = list[0]
    for n in range(1,limit):
        if check<list[n]:
            check = list[n]
    return check

size = int(input("enter the size of Array: "))
num = []
for i in range(0, size):
    num.append(int(input("Enter data: ")))
print("Largest element of the array is "+str(largest_element(num, size)))
