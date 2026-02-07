def check_disarium(num):
    n=1
    sum = 0
    for i in num:
        sum += int(i)**n
        n+=1
    if sum == int(num):
        return True
    else:
        return False

user_input = input("Enter the number: ")
if check_disarium(user_input):
    print("The given number is a disarium number.")
else:
    print("The given number is not a disarium number.")
