# The code will produce an error as the third parameter should have a default 
# value.

def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)