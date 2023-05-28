#Iteration
# Version 1.
text = "This is some generic text"
index = 0
while index < len(text):
    print(text[index])
    index += 1

# Version 2. Pythonic code
for character in text:
    print(character)