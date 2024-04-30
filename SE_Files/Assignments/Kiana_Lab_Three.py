# KIANA KOOSHESH'S LAB3 Exercises - weeks 6 to 10 :

import random

# Importing random module so we could use it later on for creating a random number in exercise 2 of week 8 & last
# question

'''
Lab 3_ Exercise 1.1 - Week 6
1. Create 3 favorite things about you using multiline string 
'''
print("== Lab 3_ Exercise 1.1 of - Week 6: ==")
kianas_favs = """coding,
photography,
watching YT,
"""  # Storing my three fav things in a multiline string
print(f"Kiana's three fav things: {kianas_favs}")  # Responsible for printing out the info stored in the kiana_favs

# === Lab 3_ Exercise 1 - Week 6's Expected Output: ===
'''
Kiana's three fav things:
coding, photography,
watching YT
'''
# == ==== ==== ===== ==== ===== ===== ===== === === ==


'''
Lab 3_ Exercise 1.2, Using variables in string print - student full details . ( firstname,lastname, address)
'''
student_firstName = "Kiana"  # Storing my first name in the student_firstName variable
student_LastName = "Kooshesh"  # Storing my last name in the student_firstName
student_address = "Richmond Hill, ON"  # Storing my address in the student_address variable
print(f"== Lab 3_ Exercise 1.2 of - Week 6: ==\n")
print(f"Student's Details:\n-Student's Firstname: {student_firstName}\n-Student's Lastname: {student_LastName}\n-Student Adress: {student_address}\n")  # Using \n to move to a new line + example usage of f string which I've used throughout my code
# Responsible for printing out student full details to the console (which here is student is me)

# == Lab 3_ Exercise 1.2 - Week 6's Expected Output: ==
'''
Student's Details:
-Student's Firstname: Kiana
-Student's Lastname: Kooshesh
-Student Adress: Richmond Hill, ON
'''
# ==== ==== ==== ===== ==== ===== ===== ===== === === ==


'''
Exercise 2 - Week 6
Create a list of agile software .Insert the values , delete one item from the list . use slicing and display the list of software's  
Exercise 3
'''
print("== Lab 3_ Exercise 2 of - Week 6: ==")
Agile_Sofrwares = ["Miro", "Jira", "Asana"]  # Creating the Agile_Softwares List
Agile_Sofrwares.insert(0,"Trello")  # Responsible for inserting a new value ("Trello") as a first element to the "Agile_Sofrwares" list at the index 0 (index 0 being the first index cause we count the values from 0 not 1)
# so this makes "Trello" our first item/ value in the list instead of "Miro" being the first value

Agile_Sofrwares.insert(1,"Proggio")  # Responsible for inserting a new value ("Proggio") at the second index to the "Agile_Sofrwares" list at the index  (index 0 being the first index cause we count the values from 0 not 1)
# so this makes "Trello" our first item/ value in the list instead of "Miro" being the first value

print(Agile_Sofrwares)
# Printing out our updated listd to the terminal after having inserted new items to it
# Expected output: ['Trello', 'Proggio', 'Miro', 'Jira', 'Asana']


print(Agile_Sofrwares[1:4])  # Responsible for slicing from index 1 to 3 the Agile_Softwares list_ Expected Output: ['Proggio', 'Miro', 'Jira']
del Agile_Sofrwares[-1]  # Responsible for deleting the last element in the list
print(
    Agile_Sofrwares)  # Printing out the Agile_Softwares list after all the modifications with expected out being: ['Trello', 'Proggio', 'Miro', 'Jira']

'''
Lab 3 - Exercise 3 - Week 6 
Start with the list by printing three courses name like comp100, comp120, comp213.
Print a message saying that you are enrolled in that course.
The text of each message should be the same, but each message should be personalized with the courses name.
Append a new course.
'''

print(f"\n== Lab 3_ Exercise 3 of - Week 6: ==")

# Storing three courses in the KianasCourses list and then printing out the list to the console:
KianasCourses = ["COMM161", "COMP120", "GNED232"]
print(f"\n{KianasCourses}")

print(f"\nKiana's enrolled in the course: {KianasCourses[0]}")  # Prints out the first element of the list which is COMM161
print(f"\nKiana's enrolled in the course: {KianasCourses[1]}")  # Prints out the second element of the list which is COMP120
print(f"\nKiana's enrolled in the course: {KianasCourses[2]}")  # Prints out the third element of the list which is GNED232
KianasCourses.append("MATH175")  # Using .append() to insert a new element(MATH175) to end of the list
print(f"\n{KianasCourses}")  # Printing out the list again after all the modifications we made to it

# Exercise 3 of week 6's expected output: ===
'''
['COMM161', 'COMP120', 'GNED232']

Kiana's enrolled in the course: COMM161

Kiana's enrolled in the course: COMP120

Kiana's enrolled in the course: GNED232
'''
# == === === ==== === ==== === === === === ==

'''
Exercise 1 - Week 8
Use the following dictionary and answer the question 
favorite_languages = {
    'jen': 'HTML',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'C#',
}
Change the value from C# to Python for the key phil 
Add an item in the dictionary 
Remove an item from the dictionary
List all the values in the dictionary 
'''
print(f"\n== Lab 3_ Exercise 1 of - Week 8: ==")

# Firstly Creating a dictionary called favorite_languages:
favorite_languages = {
    'jen': 'HTML',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'C#',  # Key = Phill,Value = C# (example of demonstration of keys and values)
}

favorite_languages['phil'] = 'Python'  # Modifiying the the value from C# to Python for the key phil
favorite_languages['Kiana'] = "C++"  # Adding an item to the Dictonary (With Kiana being the Key and c++ being the value)
print(favorite_languages)  # Printing out our dictionary after some changes (To showcase the things we altered)
favorite_languages.pop("jen")  # Using the .pop() Method to remove the item Jen
print(favorite_languages)
# Expected output after excution of the above code section:
# {'jen': 'HTML', 'sarah': 'c', 'edward': 'ruby', 'phil': 'Python', 'Kiana': 'C++'}
# {'sarah': 'c', 'edward': 'ruby', 'phil': 'Python', 'Kiana': 'C++'}

# Listing all the values of the favorite_languages using .values() method and then storing them in the favorite_Languages_Values and printing them out to the console:
favorite_Languages_Values = favorite_languages.values()
print(f"\nValues of favorite_languages:\n{favorite_Languages_Values}\n")
# Expected Output - Values of favorite languages:
# dict_values(['c', 'ruby', 'Python', 'C++'])

'''
Week 8 - Exercise 2:
create  a python dictionary called student .
Include student name, age, subject, semester, grade and lab keys. 
Include the value for each key accordingly. Display keys separately and values separately in the print statement 
'''
print(f"\n== Lab 3_ Exercise 2 of - Week 8: ==")

# Creating a Dictionary called student:
# I've indentfied/ commented out only 1 example of keys and values (Just for the purpose of displaying) but not for all of them

student = {
    "Student Name": "Kianaa",
    "Student Age": random.randint(18, 22),
    # Using .randint() from the random module we imported to genarate a random number for my age in range of 18 - 22 (Cause OFC my is between these 2 numbers)
    "Subject": "Math",
    "Semster": 1,  # Key: Semster, value : 1
    "Grade": "A+",
    "Lab": 8,
}

print("Student Keys:")

for studentKeys in student:
    print(studentKeys)
# Iterating over the "student" dictionary using for loop in order to get the keys, then we'd print the keys out
# Expected output: Student name, Student Age, Subject,Semster, Grade, Lab
# We can alterentively use:
# keysInStudentList= list(student.keys())
# print(keysInStudentList)


# Listing all the values of the student_values using .values() and printing them out to the console:
student_Values = student.values()
print(student_Values)  # Expected output: dict_values(['Kianaa', 18, 'Math', 1, 'A+', 8])

'''
Week 9 - Exercise 1:
Write a program in python using if condition . Input the temperature (user input) . Check if the temperature is less than 98 display the result as cold. otherwise  if the temperature more than 98 , display the result as Hot . otherwise display them as normal . 
'''
print(f"\n== Lab 3_ Exercise 1 of - Week 9: ==")
temperatureInput_reciver = float(input("please enter a tempreture:\n"))  # Asking for the user to input a tempreture and then converting the user input to float
if temperatureInput_reciver < 98:
    print("The weather's cold!")
elif temperatureInput_reciver > 98:
    print("The weather's hot!")
else:
    print("The weather's normal!")

# Checking if the user input number is less than 98 it says the wether's cold
# Then checks to see if the wether's more than 98 it prints out the weather's hot
# Otherwise (Like in case wether's 98 it would say the weather's normal)

# Expected output of the question could differ based on what user inputs cause of the reasons explained above.

'''
Week 9 - Exercise 2:
# Program to iterate agile values  through a list using indexing. create the following agile values in list. use for loop and iterate over the list 

agile_values = ['Individuals and interactions', 'Working software ', 'Customer collaboration ','Responding to change']
'''
print(f"\n== Lab 3_ Exercise 2 of - Week 9: ==")
agile_values = ['Individuals and interactions', 'Working software ', 'Customer collaboration ', 'Responding to change']

print("\nAgiles values are:")
for v in range(len(agile_values)):
    print(f"Agile Value {v + 1}: {agile_values[v]}")

'''
Creating a for loop to and the using range(len(iterable)) since the question asked for iterating through
Agiles_valusspecificlly using indexing ( and I know it's more than what we learned in the class I thought 
since we were asked to iterate using indexing) asimple for loop wouldn't be enough), explanation below:
'''
# The  range(len(iterable)) is basiclly a combo of len(agile_values) and range() & is responsible for creating from 0 to the length of the agile_values list - 1 (Which for my case would be 3 cause I have 4 elements).
# We use {v+1} for getting/ refrering to the index numbers of each item which we were able to achieve through range(len(iterable)) in the list & the {agile_values[v]} to get the agile values themselves

'''
Expected output for exercise 2 of week 9:
Agiles values are:
Agile Value 1: Individuals and interactions
Agile Value 2: Working software 
Agile Value 3: Customer collaboration 
Agile Value 4: Responding to change
'''

'''
Week 10 _ Exercise 1: 
Create a function called team_collaboration() . pass two team collaboration software names as the arguments. 
The function should print "I use ------- software for team collaboration "
'''

print(f"\n== Lab 3_ Exercise 1 of - Week 10: ==")


# Creating a function called team_collaboration with two parameters
def team_collaboration(collabrationSoftware1, collabrationSoftware2):
    print(f"\nI use {collabrationSoftware1} software for team collaboration \n")
    print(f"I use {collabrationSoftware2} software for team collaboration \n")


team_collaboration("Slack", "GitHub")  # Passing 2 collabration softwares as arguments and calling the function

# Expected output:
# I use Slack software for team collaboration
# I use GitHub software for team collaboration

'''
Week 10 - Exercise 2:
Create a function called project() that store project_id globally and locally . Call the function and display both the id's . 
Print the statement as 
"My global project id is :"
"My internal project id is :"
'''
print(f"\n== Lab 3_ Exercise 2 of - Week 10: ==")

# Our global variable which is defiened outside the function and has a global scope:
global_project_id = random.randint(1000,10000)  # Using .randint() to generate a random number between the rang of 1000 and 10000 and assining that random number to the global_project_id


def project():
    local_project_id = 8929  # Creating a local variable and assining a number to it
    print(f"My gloabal project id is: {global_project_id}")  # Responsible for printing out the global id (cause OFC the local variable should be inside the function), expected output:a random 4 digit number between 1000 and 10000
    print(f"My local project id is: {local_project_id}")  # Responsible for printing out the local id, expected output: 8929


project()  # And finally calling our function which is essential for execution of the code and receiving output

# Expected out put:
# My global project id is: some random 4 digit number between 1000 and 10000
# My local project id is: 8929
