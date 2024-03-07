counter = 0

while counter < 5:
    print(counter)
    
# The above code creates an infinite loop because the variable counter is 
# assigned the value of 0 and the while loop on line 3 checks if `counter` is 
# less than 5. This means that the condition for the while loop to be `True` 
# is indefinitely active. To fix this one would need some code inside the 
# while loop that would eventually make `counter` greater than 5.