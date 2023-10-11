#Logical operators (and, or, not) is used to check if two or more conditional statements are true

#USING 'AND' 'OR'
#temp = int(input("Enter the temperature: "))
#if temp >= 0 and temp <= 30:
#   print("The temperature is good today!")
  #  print("Stay inside!")
#elif temp < 0 or temp > 30:
#   print("The temperature is bad today!")
  #  print("Stay inside!")

#USING 'NOT'
#temp = int(input("Enter the temperature: "))
#if not (temp >= 0 and temp <= 30):
#   print("The temperature is good today!")
  #  print("Stay inside!")
#elif not (temp < 0 or temp > 30):
#    print("The temperature is bad today!")
#   print("Stay inside!")
#both conditions are required to be true when using; and 

#def input(fname, lname):
#    pass

#def greet(fname, lname):
#    print("hello ",fname, lname)

def birthday ():
    print ("Happy birthday to you")

def wish (name):
    birthday ()
    birthday ()
    print ("Happy Birthday ", name)
    birthday ()

name = input("Enter you name: ")
wish (name)