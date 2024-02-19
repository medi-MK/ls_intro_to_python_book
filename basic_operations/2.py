"""
This question may be a little challenging if your math skills are rusty. 
Don't be afraid to take advantage of the hints. Try your best to solve 
the problem, but don't feel compelled to complete it if you become frustrated.

Use the REPL and the arithmetic operators to extract the individual digits of 4936
"""

starting_number = 4936
one_place = starting_number % 10
second_number = (starting_number - one_place) / 10
tens_place = int(second_number % 10)
third_number = (second_number - tens_place) / 10
hundreds_place = int(third_number % 10)
thousands_place = int((third_number - hundreds_place) / 10)

print(f''' 

One place is {one_place}.
Tens place is {tens_place}.
Hundreds place is {hundreds_place}.           
Thousands place is {thousands_place}.
           
''')
           
           
           

           
