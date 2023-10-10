def get_value():
    return "Hello"

value = get_value
print(value)

numbers = [10, 12, 24, 35, 7]
def find_smallest(numbers):
   min_number = min(numbers)
   return min_number
value= find_smallest(numbers= numbers)
print(value)

x = list 
print (x)
def square(*args):
    retlist = []
    for num in args: 
        retlist.append(num**2)
    return retlist 

values = square(3, 4, 6 ,8)
print (values) 

def average(lst):
    if len(lst) == 0:
        return None
    sum_of_list = 0
    for i in range (len(lst)):
        sum_of_list += lst[i]
    average = sum_of_list/len(lst)
    return average 

value = average(numbers)
print(value)

def count_vowels(str):
    count = 0
    vowels = ["a", "e", "i", "o", "u"]
    for i in range(len(str)):
        if str [i] in vowels:
            count +=1

    return count 
value = count_vowels("Hello, World!")
print(value)