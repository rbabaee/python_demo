a = 'a'
a = "a"
a = """this
is
a 
multi-line
string"""
a = ''' you can also write me like this'''

# white space between string literals is ignored . for example:

print("hell" "o" == "hello")
# all strings in python 3 are unicode. in python 2 you should have written unicode strings like u'some unicode'
# a lot of useful string methods!

test_string = 'This is a TEST string!'

print(test_string.capitalize())
print(test_string.lower())
print(test_string.endswith('h'))  # there is also startswith
print(test_string.count('i'))
print(test_string.center(50))
print(test_string.casefold())  # casefold is used for comparison.
print('splitting a string with spaces:\n\t{}'.format('this is a sentence').split(' '))

# a lot of other builtin string methods, including title, swapcase, upper and ...
