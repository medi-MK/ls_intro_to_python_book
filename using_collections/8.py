text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29

# It prints different values because on line 3 we are using slicing to create 
# a new string and the `rfind` method is indexing from the beginning of that 
# new string. The code on line 4 however is using the `rfind` method with 
# arguments which search between indexes 21 and 35 but still count from the 
# beginning index of the original string