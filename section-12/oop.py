class Person(object):
  def __init__(self, person):
    deserialized_person = self.deserialize(person)
    self.first_name = deserialized_person['first_name']
    self.last_name = deserialized_person['last_name']
    self.email = deserialized_person['email']

  def serialize(self):
    return {
      'firstName': self.first_name,
      'lastName': self.last_name,
      'email': self.email
    }
  
  def deserialize(self, person):
    return {
      'first_name': person.get('firstName', None),
      'last_name': person.get('lastName', None),
      'email': person.get('email', None),
    }

anthony = Person({
  'firstName': 'Anthony',
  'lastName': 'Scinocco',
  'email': 'anthony1@mail.io'
})

print(anthony.serialize())
