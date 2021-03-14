"""
Makroscale->Usable Easy Program
How many percent is the value of x in relation to value y
"""
def Calcfrom_str(*args,):
    print('How many percent is the value of x in relation to value y')
    x = input("How value is (x)? ")
    y = input('Relative to what value (y)? ')
    return print(f'{x} is {round(((int(x)/int(y))*100), 5)}% from {y}')
Calcfrom_str()
