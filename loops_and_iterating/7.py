# def find_integers(a_tuple):
#     integers = []
#     for element in a_tuple:
#         if type(element) == int:
#             integers.append(element)
            
#     return integers
        
def find_integers(a_tuple):
    return [element 
            for element in a_tuple 
            if type(element) == int]
    
    




my_tuple = (1, 'a', '1', 3, [7], 3.1415, -4, None, {1, 2, 3}, False)
integers = find_integers(my_tuple)
print(integers)

