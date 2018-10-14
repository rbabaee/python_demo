"""
 if statements
"""

fav_color = 'Blue'
rainbow_colors = ['Violet', 'Indigo', 'Blue', 'Green', 'Yellow', 'Orange', 'Red']

if fav_color in rainbow_colors:
    print('My favorite color is in rainbow colors!')

age = 13

if 13 <= age <= 19:
    print('you are a teenager')
elif age == 20:
    print('Yay! you are 20 years old!')
elif age <= 90:
    print('You are an adult!')
elif age > 90:
    print('Congrats! you are a grandparent!')
else:
    print('umm ... you must have entered a wrong number as your age!')
# Python has no switch case statement.

a = ''

if a:
    print('a is considered True')
else:
    print('a is considered False!')

# false values in python are False, None, 0 ( with every possible presentation, as complex, integer, float and etc),
# and empty lists, tuples, dictionaries or strings.
