# The code doesn't print anything as the `print` statement occurs
# after the function returns

def scream(words):
    words = words + '!!!!'
    return
    print(words)

scream('Yipeee')