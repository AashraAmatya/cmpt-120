#slicing strings in python
#slicing = creating a substring by extracting elements from another string 
# slicing can be performed either 
#indexing: [] or slice: ()
#with slicing there are 3 optional arguments [start:stop:step]

#for starting index and ending index
#name = "Aashra Amatya"
#first_name = name[0:6] 
#OR could be written as
#first_name = name[:6]
#last_name = name[7:13]
#OR could be written as
#last_name = name[7:]
#print(first_name)
#print(last_name)
#1st index is inclusive, 2nd index is exclusive

#print every second character of the word "Aashra Amatya"
#name = "Aashra Amatya"
#sec_alp = name[0:13:2]
#OR can be written as
#sec_alp = name[::2]
#print(sec_alp)

#reverse a string in lower case 
#name = "Aashra"
#name = name.lower()
#reverse_name = name[::-1]
#print(reverse_name)

#using the slice() 
#slice can only handle upto 3 values; start, stop, step
#website1 = "http://google.com"
#website2 = "http://wikipedia.com"
#slice = slice(7,-4) #using a negative to count for the end values 
#print(website1[slice])
#print(website2[slice])

website1= "http//google.com"
website2= "http//wikipedia.com"
slice = slice(6,-4)
print(website1[slice])
print(website2[slice])
