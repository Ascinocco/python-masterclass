for i in range(1, 12):
  print('the number is: ' + str(i))

sometimesDogsAre = input("Some times dogs are? ")

if sometimesDogsAre == 'brown':
  print('hehehe :P')
elif sometimesDogsAre != 'brown':
    print('that dog is not brown!')
else:
  print("You entered something that is pure evil, didn't yoou")

if (True != False) and (False != True):
  print('lol')

if not 0 == None:
  print('hm?')

print(None) # is kind of like undefined
# python is also a truthy language

if 5 == True:
  print('5 == True')
elif 0 == False:
  print('0 == False')
elif (bool(0) == False):
  print('bool(0) == False')

evaldBool = bool(0)

if evaldBool == False:
  print('it does')

print(bool(0))

strLength = len("abc") # 3
