my_tuple = (1, 2, 3, 4, 5)

temp_list = tuple(reversed(list(my_tuple[1:-1])))

print(temp_list)


# super unreadable solution above

# Better to use `tuple` with slice: 


my_tuple = (1, 2, 3, 4, 5)
result = my_tuple[-2:-5:-1]

