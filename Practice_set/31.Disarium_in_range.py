print("Disarium number in the range of 1 to 100 is: ")
for i in range(1,100):
    n = 1
    num = str(i)
    sum = 0
    for m in num:
        sum+= int(m)**n
        n+=1
    if sum == i:
        print(i)