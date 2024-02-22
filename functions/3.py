# Write a program that uses a multiply function to multiply 
# two numbers and returns the result. Ask the user to enter 
# the two numbers, then output the numbers and result as a 
# simple equation.

def get_number(text):
    number = input(text)
    return float(number)

first_number = get_number('Enter the first number: ')
second_number = get_number('Enter the second number: ')

def multiply(number1, number2):
    return number1 * number2

result = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {result}')

