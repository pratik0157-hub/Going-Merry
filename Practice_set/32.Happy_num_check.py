history = []
num = int(input("Enter any number: "))

while num != 1 and num not in history:
    history.append(num)

    dummy = num
    sum = 0
    while dummy>0:
        digit = dummy%10
        sum+= digit**2
        dummy //= 10
    
    num = sum

if num == 1:
    print("The given number is a happy number.")
else:
    print("The given number is not a happy number.")