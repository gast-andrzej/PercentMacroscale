"""
Makroscale->Usable Easy Program
What is x percent of the value of y
"""

def Percent_Str(*args,):
    print('What is x percent of the value of y')
    x = input("How many percent (x) ")
    y = input('From what value (y)? ')
    return print(f'{x}% from {y} is {round((int(x)*(int(y)/100)), 5)}')
Percent_Str()
