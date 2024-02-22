# The code will print `bar` as the variable `foo` is defined
# in the global scope and also called in the global scope.  

foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)