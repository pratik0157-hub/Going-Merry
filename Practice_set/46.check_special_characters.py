def special_character(text):
    special = r'@_!#$%^&*()<>?/\|}{~:'
    
    for ch in text:
        if ch in special:
            return True
    return False

        
words = input("Enter the  first sentence: ")
print(special_character(words))