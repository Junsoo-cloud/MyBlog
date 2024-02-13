# Strcuture of a class


class Person(object):

  def __init__(self, name, idnumber):
    self._name = name
    self._idnumber = idnumber


per_1 = Person("Junsoo", 1234)
print(per_1)
