nums = [1, 2, 3, 4, 5]

#1lambdas
#square = lambda x: lambda x: x**2


#squared_nums = list(map(lambda x: x**2, nums))
#print(squared_nums)

#regular functions 
#squared_nums = []
#for i in nums: 
    #squared_nums.append(i**2)
#print(squared_nums)

#2methods 
#nums.clear()
#print(nums)

#class MyClass: 

    #def__int__(self): 
    #self.my_name = "My name!"

#def get_my_name(self):
    #return self.my_name 

#4constructor
#my_class = MyClass()
#print(my_class.get_my_name())

#def my_function(a: int, b="hello"):
    #if type(a) != int:
        #raise Exception ("wrong parameter type!", type(a))
    #for i in range(len(a)):
        #print(b)

#def get_two():
    #return 1, 2

#a, b = get_two()
#print(a)
#print(b)

#vals = get_two()
#a = vals[0]
#b = vals[1]
#print(vals)
#print(a)
#print(b)

#def get_stuff(x="five"):
    #return x, ["1, 2", 3, True], False

#Pass by value 
#x = 3
#print(x)
#def add_3(x):
    #return
#print(add_3(x))
#print(x)

#pass by reference 
#my_list = []
#print(my_list)

#def add_something(l:list, thing: any):
    #l.append(thing)

#add_somehting(my_list, "kelvin")
#print(my_list) 


#from unittest import *
#import pytest 

#class TestSuite:

    #def test_00(self):
        #x=  5
        #x = plus_five(x)
        #assert x==10

#def test_01(self):
   #x = None
    #with pytest.raises(TypeError):
        #x = plus_five(x)

#def test_04(self):
    #email = "jane.smith@fakeemali.com"
    #add_email(email)
    #assert email in get_emails()

    #def test_05(self):
        #email = "john.smith@fakeemail.com"
        #with pytest.raises(Exception):
            #add_email(email)
        #assert len(get_emails()) ==2
