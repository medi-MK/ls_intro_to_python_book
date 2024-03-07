my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]




list_index = 0
while list_index < len(my_list):
    num = 0
    while num < len(my_list[list_index]):
        if my_list[list_index][num] % 2 == 0:
            print(my_list[list_index][num])
        num += 1
        
     
    list_index += 1


