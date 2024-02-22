# There will be an error message as the `print` is trying to 
# print the variable `foo` which is only available in the function
# scope of `set_foo`

# heres how to fix it:

def set_foo():
    foo = 'bar'
    return foo

set_foo()
print(set_foo())
