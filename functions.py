def HelloWorld():
  print("Hello world!")

HelloWorld()

def Greeting(name):
  print("Hello " + name + "!") 
Greeting("gagas")

def Add(num1, num2):
  return num1 + num2
  # below this never executed
  print("test")
print(Add(10,15))