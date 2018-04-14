# list === array
# list can be a sequence of lists (assoc array)

# -------------------------- LISTS ----------------------
phrase = [
  'your',
  'mother',
  'is',
  'a',
  'lovely',
  'person'
]

phrase.append('hit me baby one more time, bang bang')

for word in phrase:
  print(word)

numbers = [6, 1, 7, 33, 12, 9, 10, 0]
#numbers.sort()
#print(numbers)

newNumbers = sorted(numbers) # how can i specify sort criteria here?
print(newNumbers)

if numbers == newNumbers: # seems like == will handle a shallow compare
  print('numbers lists are equal')
else:
  print('numbers are not qual')

# list using constructor
anotherList = list()
listAgain = []
# there is no difference in practice

# reversing an array is really simple in pything
even = [2, 4, 6, 8]
newReverseEven = sorted(even, reverse=True) # this sorts the array and returns a new array so that the original is not modified
evenAgain = even # assings reference of even to evenAgain
even.sort(reverse=True)
print(even)
print(evenAgain) # both will be sorted since the variable is evenAgain contains a reference to even instead of a copy of the values
# -----------------------------------------------------------------

print(False or True) # you need to use 'or' instead of || in python... who knows why
print(False is True)

# Also quick note on structure comparison in python
one = 1
oneAgain = one

aDifferentOne = 1

if one is oneAgain:
  print('Yes it is, because they reference the same original value')
elif one == aDifferentOne:
  print('Yes one does ==  aDifferentOne because the have the same value')
elif not (one is aDifferentOne):
  print('one is not aDifferentOne because they dont reference the same original variable')


# you can merge two lists by doing the following
listone = [1,2,3]
listtwo = [4,5,6]

mergedlist = listone + listtwo
# it's really that nice

letters = ['a', 'b', 'c']
for letter in letters:
  if not 'a' in letter:
    print(letter)
