# User inputs and Prints
# num1 = input('Enter a number ')
# num2 = input('Enter a number ')
# sum = float(num1) + float(num2)
# print(sum)


# Lists
people = ["bob", "Karen", "travis"]

print(people[1])
people.reverse()
print(people)
twodlist = [
  [1, 2],
  [3, 4]
]
print(twodlist[0][1])
 
# dictionary
bob = { 
  'test': 3,
  'test2': 2
}
print(bob['test2'])


# function
def test(number):
  print('test: ' + str(number))

test(2)

# Classes
class Student:

  def __init__(self, name, major, gpa):
    self.name = name
    self.major = major
    self.gpa = gpa
  
  def on_honor_roll(self):
    if self.gpa >= 3.5:
      return True
    else:
      return False

alex = Student('alex', 'IT', 4.0)

print(alex.major)
print(alex.on_honor_roll())