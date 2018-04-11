# list === array
# list can be a sequence of lists (assoc array)

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
