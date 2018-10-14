# python for statements are equivalent to foreach statements in other languages
# remember our rainbow_colors list?
rainbow_colors = ['Violet', 'Indigo', 'Blue', 'Green', 'Yellow', 'Orange', 'Red']

for r in rainbow_colors:
    print(r)

# you can control for loops with continue, and break like in other languages
for r in rainbow_colors:
    if 'e' in r:
        continue
    if r == 'Orange':
        break
    print(r)

# but, what if I NEED indexing?

for r in enumerate(rainbow_colors):
    print('color number {} is {}'.format(*r))

# but, what if I just need to do for loops like I used to do before?
# You probably don't need that, but you can do that since python is just awsome!

for r in range(len(rainbow_colors)):
    print('color number{} is {}'.format(r, rainbow_colors[r]))

# range is a builtin function
# Python has a for-else statement. you can use for else for the time you are looking for something in a for loop
# and you break the loop when you find it. else statement runs when break is not run.

for r in rainbow_colors:
    if r == 'purple':
        break
else:
    print('purple is not in rainbow colors!')

# or a more serious example:
# finding prime numbers between 2 and ten.
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n / x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# range swith step
for n in range(2, 30, 3):
    print(n)

# while loops
i = 1
while i in range(1, 10):
    print(i)
    i += 1
