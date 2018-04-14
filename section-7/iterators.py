from copy import deepcopy

# Yay iterators!
something = [
  '1', '2', '3'
]

# you can get the index of an item in an array like so
print(something.index('1'))

for (i, some) in enumerate(something):
  print(str(i) + ' ' + str(some))


# so here is how to make an iterator
someIterator = iter(something)

# prints out the next element in an iterable
print(next(someIterator))
print(next(someIterator))

# when checking the copy's with the `is` operator it will be false because copy returns new objects
shallowSomething = something.copy() # returns a new shallow copy of the list
deepSomething = deepcopy(something) # returns a deep copy of something | Also, deep copy must be explicitly imported

matches = list(filter(lambda some: some == '1', deepSomething)) # this is a little annoying, es6 handles filtering much nicer

print(matches)

# there is also a mapping function
yourMothersFavouriteNumbers = [5, 6, 7]

mappedNumbers = list(
  map(
    lambda number: number + 1, yourMothersFavouriteNumbers
  ) # not bad but still not as clear as es6, why explicitly state it is a lambda???
) # it burns my soul that I have to wrap maps in list constructor... I guess they do this so you can assign it to
# Any iterable type?


print(mappedNumbers)
