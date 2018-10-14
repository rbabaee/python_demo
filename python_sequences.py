# sequence is an ordered set.
# python sequences include list, tuple, range, text strings
# sequence operations:
# in and not in, * ( adding to itself n times ), s[i] , s[i:j:k] is slicing from i to j with step k
# len, max, min, s.count(x),
# there are also del s[i:j:k], s.clear() (removes all), s.copy(), s.extend(t)--> s+=t
# s.pop([i]) --> retrieve and remove i from list
# s.reverse() --> reversing list items
# s.remove(x)

"""
note:
>>> lists = [[]] * 3
>>> lists
[[], [], []]
>>> lists[0].append(3)
>>> lists
[[3], [3], [3]]

because * adds one object 3 times.
"""

x = list(range(0, 11))

print('element in index 1 is {}'.format(x[1]))
print('elements from index 0 to 5 are :\n\t {}'.format(x[0:5]))
print('elements from index 5 from the END untile index 1 from the end are: \n \t {}'.format(x[-5:-1]))
print('elements from index 2 to index 6 with 2 steps are:\n\t {}'.format(x[2:6:2]))
print('elements from start to end with steps of size 2 are:\n\t {}'.format(x[::2]))
print(x * 2)
print('number of  "e"s  in "Advanced Computer Networks" is:\n\t {}'.format(("Advanced Computer Networks").count('e')))

# python lists and tuples
# tuples are immutable, mostly for heterogeneous data
# lists are mutable mostly for homogeneous data

print(' '.join(['hello', 'this', 'is', 'a', 'sentence']))
