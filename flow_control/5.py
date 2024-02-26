def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([])


# The code outputs 'Empty' as the `if` statement on Line 2 is checking 
# whether the `my_list` is a truthy.  `my_list` is an empty list which is 
# evaluated as falsy value and therefore the code will print 'Empty'