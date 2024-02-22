def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# multiply: 1, 9
# left, right: 1
# get_num: 4, 7, 8
# prompt: 4, 5
# float: 5
# input: 5
# print: 10