class Student:
  def __init__(self, name, grade=0):
    self.name = name
    self.grade = grade

  def setGrade(self, grade):
    self.grade = grade