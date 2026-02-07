line = input("Enter the sentence: ")
final = " "
n = 0
punctuation_chars = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
for char in line:
    if char not in punctuation_chars:
        final = final + char

print(final)
