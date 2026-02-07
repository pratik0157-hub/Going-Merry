def lcm(num1, num2):
    if num1>num2:
        greater = num1
    else:
        greater = num2
    while True:
        if (greater%num1==0) and (greater%num2==0):
            ans = greater
            break
        greater+1
    return ans
total = int(input("Lowest Common Multiple of how many numbers: "))
if total>=2:
    num = []
    for i in range(1, total+1):
        num.append(int(input("Enter number "+str(i)+": ")))
    final = num[0]
    for n in range(1, total):
        final = lcm(final, num[n])
    print("LCM of the given numbers is "+str(final))
else:
    print("There must be atleast two numbers")

