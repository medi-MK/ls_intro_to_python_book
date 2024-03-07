def find_factorial(input):
    tally = 1
    for num in range(1, input + 1):
        tally *= num
    return tally


print(find_factorial(5))

