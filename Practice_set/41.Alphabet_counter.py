def counter_check(arr, limit):
    final = []
    for item in arr:
        if len(item)>limit:
            final.append(item)
    
    return final
words = list(input("Enter the sentence: ").split())
print(counter_check(words, 3))