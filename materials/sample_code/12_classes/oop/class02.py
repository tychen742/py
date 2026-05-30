##### The __init__() Function #####
##### __inti__() assigns the values to object properties.
##### Note: The __init__() function is called automatically every time the class is 
##### being used to create a new object.

##### this is p1.XXXXX
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)   ### just like function

# print(p1.name)
# print(p1.age)


##### compare these two:

class Person2:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p2 = Person2("Jessica", 26)

# print(p2)
# print(p2.name)
# print(p2.age)


##### compare with the above
class Person3:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"   ### format string

p3 = Person3("John", 36)

# print(p3)

class Time:
    """Represents the time of day."""    

    def print_time(self):
        s = f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'
        print(s)
        
def make_time(hour, minute, second):
    time = Time()
    time.hour = hour
    time.minute = minute
    time.second = second
    return time

lunch_time = make_time(12, 13, 14)
Time.print_time(lunch_time)


class  Home:
  def  __init__(self, rooms, stories):
    self.rooms = rooms
    self.stories = stories

  def  __str__(self):
    return  "The house has {} rooms and {} stories".format(self.rooms, self.stories)

home = Home(4, 2)
home.address = "1234 Oak Street"

# print(home)
print(str(home))
print(home.__str__())

# print(home.address)

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    # print(self.firstname, self.lastname)
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

# x = Person("John", "Doe")
# x.printname()

# class Student(Person):
#   pass

# y = Student("TY", "Chen")
# y.printname()
# print(y.firstname)
# print(y.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)  ### "super" inherits all attributes
    self.graduationyear = year      ### customized attribute

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
    
st = Student("John", "Doe", 2025)
# st.welcome()



class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

# for x in (car1, boat1, plane1):
#   print(x.brand, end=" ")
#   print(x.model, end=" ")
#   x.move()

class Mynumber:
    def __init__(self, value):
        self.value = value
    
    def print_value( ):
        print(value)

# obj1 = Mynumber(17)
# obj1.print_value()

