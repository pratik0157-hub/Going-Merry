def uncommon(s1, s2):
    final = []
    for item in s1:
        if item not in final:
            final.append(item)
    

    for item in s2:
        if item not in final:
            final.append(item)
        
    return final
sentence1 = list(input("Enter the  first sentence: ").split())
sentence2 = list(input("Enter the second sentence: ").split())

print(uncommon(sentence1,sentence2))