num = int(input("Enter the sum of naturals numbers upto which number: "))
sum = 0
for i in range(0, num+1):
    sum+=i
print("Sum of natural numbers upto", num,"is",sum)