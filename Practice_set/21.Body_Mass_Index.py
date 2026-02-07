def BMI(w, h):
    ans = w/(h*h)
    return ans

weight = int(input("Enter the weight(KG): "))
height = int(input("Enter the Height(m): "))
print("Body Mass Index is "+str(BMI(weight, height)))


