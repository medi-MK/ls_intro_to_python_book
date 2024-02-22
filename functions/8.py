# The code will output an error as the function call is giving 
# too many arguments to match the parameters of the function
# definition 

def foo(bar, qux):
    print(bar)
    print(qux)

foo(42, 3.141592, 2.718)