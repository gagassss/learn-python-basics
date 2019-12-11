class Parent:
  def __init__(self):
    print("this is the parent class")
  def parentFunc(self):
    print("this is the parent func")
  def test(self):
      print("Parent")

class Child(Parent):
  def __init__(self):
    print("this is the Child class")
  def childFunc(self):
    print("this is the child func")
  def test(self):
    print("child")
    
p = Parent()
c = Child()
c.parentFunc()
c.test()
