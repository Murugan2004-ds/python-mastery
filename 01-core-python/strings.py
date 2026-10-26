text = " Hello,AI Engineer "

# clean the text
print(text.strip())
print(text.lower())
print(text.replace("AI","ML"))


# slicing works just like lists
word = "Python"
print(word[0])
print(word[-1])
print(word[0:3])
print(word[::-1])

# split and join
sentence = "learn python every day"
words = sentence.split()
print(words)
print("-".join(words))
