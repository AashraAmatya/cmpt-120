first_name = input("Enter you first name: ")
last_name = input("Enter your last name: ")
first_initial = first_name [0]
first_five_the_last = last_name [0:5]
email = first_initial + "." + first_five_the_last + "@marist.edu"
print (email)