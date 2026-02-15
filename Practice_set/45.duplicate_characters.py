def counter(arr):
    type = {}
    for item in arr:
        if item in type:
            type[item]+=1
        else:
            type[item]=1
    return type

def duplicate(arr):
    duplicate = []
    for item in arr:
        if arr[item]>=2:
            duplicate.append(item)

    return duplicate

words = list(input("Enter the  first sentence: ").split())
print(duplicate(counter(words)))