# dict's are more or less what json objects are

numbers = {
  'one': 1,
  'two': 2,
  'three': 3,
}

print(numbers)

# print(numbers['one'])

keys, values = numbers.keys(), numbers.values()

# print(keys)
# print(values)

# iterate over a dict like normal
for key in numbers:
  print(numbers[key])


# to delete a key
del numbers['one']

# now it is gone
for key in numbers:
  print(numbers[key])

# two merge 2 dicts
letters = {
  'a',
  'b',
  'c',
}

lettersAndNumbers = letters.copy()
lettersAndNumbers.update(numbers)
print(lettersAndNumbers)
