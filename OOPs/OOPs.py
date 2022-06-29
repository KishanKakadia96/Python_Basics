class myClass():
  def method1(self):
      print("Kishan")
        
  def method2(self,someString):    
      print("Software Testing:" + someString)

c = myClass()
c.method1()
c.method2("Testing is fun")

# Inheritance 

class childClass(myClass):
  def method1(self):
        myClass.method1(self)
        print ("childClass Method1")
        
#   def method2(self):
#         print("childClass method2")     

c2 = childClass()
c2.method1()
c2.method2("Inheritance")

# Python Constructors

class User():
    def __init__(self, name):
        self.name = name

    def sayHello(self):
        print("Welcome to Kishan, " + self.name)

User1 = User("Kakadia")
User1.sayHello()