def isbinary(s):
    for i in range(0,len(s)):
        if s[i]!=0 and s[i]!=1:
            return False
        
    return True

trial = input("Enter any sentence/word: ")
print("binary: ",isbinary(trial))