def remainders_3(numbers):
    return [number % 3 for number in numbers]
    
# Use this function to determine which of the following lists contains at least 
# one number that is not evenly divisible by 3 (that is, the remainder is not 0):


numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []


print(any(remainders_3(numbers_1)))
print(any(remainders_3(numbers_2)))
print(any(remainders_3(numbers_3)))
print(any(remainders_3(numbers_4)))
