# Write a function that takes a string as an argument and returns an all-caps 
# version of the string when the string is longer than 10 characters. 
# Otherwise, it should return the original string. Example: change 'hello 
# world' to 'HELLO WORLD', but don't change 'goodbye'.

def capitalise_large_strings(text):
    if len(text) > 10:
        return text.upper()
    else:
        return text


print(capitalise_large_strings('Hello world'))
print(capitalise_large_strings('goodbye'))
print(capitalise_large_strings("Sue Smith"))     # Sue Smith
print(capitalise_large_strings("Sue Roberts"))   # SUE ROBERTS
print(capitalise_large_strings("Joe Shea"))      # Joe Shea
print(capitalise_large_strings("Joe Stevens"))   # JOE STEVENS

