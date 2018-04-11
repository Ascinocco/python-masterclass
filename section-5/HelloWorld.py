__author__ = 'Anthony'
# Some super basic stuff

print('Hello World')

# greeting = 'Hello'
# name = input('Please enter your name ')
# print(greeting + ' ' + name)

multiLineString = '''
yooooo
you punk
iaojsfisajf
'''

print(multiLineString)


# here is something slightly useful
# this is more or less equivelent to js splice but way more friendly
someBoringString = 'blahblahblah'
print(someBoringString[:6]) # prints from 0 - 6 element
print(someBoringString[3:6]) # prints from 3 - 6 element
print(someBoringString[4:]) # prints from 4 - last element
print(someBoringString[0:6:3]) # prints from 0 - 6 in steps of 3

# prints out the numbers without commas or spaces
numbers = '1, 2, 3, 4, 5, 6'
print(numbers[0::3])

# you can multiply the number of times a string prints which is cool
print('you suck ' * 5)

# checking for strings in strings is pretty straight forward
youAreAPunk = 'you are a punk'
print ('punk' in youAreAPunk)

youAreNotAPunk = 'nope'
print('punk' in youAreNotAPunk)

youAreAPanther = 'panther'
print('pan' in youAreAPanther)
