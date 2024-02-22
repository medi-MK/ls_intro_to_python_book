def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')


# multiply: global
# left, right: local (to the `multiply` function)
# get_num: global
# prompt: local (to the `get_num` function)
# float, input, print: built-in
# first_number, second_number, product: global