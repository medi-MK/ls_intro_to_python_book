my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)


# 1. Yes they are equal
# 2. Yes, they are not the same object - it's a shallow copy
# 3. Yes, the nested lists are equal
# 4. Yes, the nested lists are the same object