import string

def alphaNum_generator():
    count = 1
    while True:
        for letter in string.lowercase:
            yield letter + str(count)
        count += 1
