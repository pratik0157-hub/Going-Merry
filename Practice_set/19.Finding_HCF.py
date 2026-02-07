def hcf(num1, num2):
    if num1>num2:
        smaller = num2
    else:
        smaller = num1
    for i in range(1, smaller+1):
        if (num1%i==0) and (num2%i==0):
            ans = i
        else:
            continue
    return ans
total = int(input("Highest Common Factor of how many numbers: "))
if total>=2:
    num = []
    for i in range(1, total+1):
        num.append(int(input("Enter number "+str(i)+": ")))
    final = num[0]
    for n in range(1, total):
        final = hcf(final, num[n])
    print("HCF of the given numbers is "+str(final))
else:
    print("There must be atleast two numbers")