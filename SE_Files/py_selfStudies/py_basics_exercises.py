# Q1: Using % for remainder
print("Q1.", -7 % 3, "\n")

# Q2: Performing division
print("Q2.", 10.0 / 3, "\n")

# Q3. If Else
if 2 > 3:
    print("Hello!")
print("Q3", "Bye!", "\n")

# Q4. And in Python
# Q4. Or in Python
if 2 < 3 or 4 > 5:
    print("Q4.", "AND Example's Output:" + str(2), "\n")

# Python continued - Week 6 Practice :

# Q5:
txt = "welcome to the jungle"
x = txt.split()
print(x, "\n")

# Q6:
print("Hi\n")

# Q7:
# Q8:

# Extra Points - Self Study #

# **
# Exponent 2, 4 to the power of 2:
print(4 ** 2, "\n")
# Exponent 3, 2 cubed or 2 to the power of 3
print(2 ** 3, "\n")

# +=
# += sign:
# Used for:
"""
The plus-equals operator += provides a convenient way to add a value to an existing variable and assign the new value 
back to the same variable. In the case where the variable and the value are strings, this operator performs string 
concatenation instead of addition.
The operation is performed in-place, meaning that any other variable which points to the variable being updated will 
also be updated.
"""
counter = 20
counter += 3
print(counter, "\n")

# += conactination
message = "Part 1 of message,"
message += "Part 2 of message\n"
print(message)

# % for modulus (returns the remainder)
result = 25 % 2  # Rmainder:1
print(result, "\n")

# -=
"""
We have a scenario where a player's score in a game needs to be adjusted due to a penalty for making a mistake. 
We'll utilize the `-=` operator to subtract the penalty from the player's total score.
"""

# Initial score of the player
score = 100
# Penalty for making a mistake
penalty = 20
# Applying the penalty to the player's score using the -= operator
score -= penalty
# Printing the updated score
print("Player's updated score after applying penalty:", score, "\n")

# Str()function:
# Python str() function is used to convert an object to its string representation. It is a built-in function that
# can be used to convert objects of different data types, such as integers, and floats.

# Converting int to string:
mass = 35
blackHole_mass = str(mass)

# Type() gets the data type -> str:
# print(type(blackHole_mass))

# Type() gets the data type -> int:
# print(type(mass))
print("Black Hole's mass:", blackHole_mass, "\n")

# Multi-line strings
blackHOle_facts = """
Black holes, born from the collapse of massive stars, warp space-time with their intense gravity. At their heart lies 
a singularity, where matter is infinitely dense. Even light cannot escape their event horizon, rendering them invisible.
Studying black holes unlocks mysteries of the universe and challenges our understanding of physics.
"""
# print(blackHOle_facts)

# Relational Operators - Equals: == and Not equals:
print(13 - 6 != (3 * 2) + 1)
print(3 * (2 - 1) == 4 - 1, "\n")

# If else Practice:
# Note - Elif should always be used before else statement:
gitHub_user = "Kiana"
if gitHub_user == "Kiana":
    print("Practices Python!")
elif gitHub_user == "Mike":
    print("Is a backend developer!")
else:
    print("Practices another programming language!")

# Not, and, or in if else statements:
studentCredits = 120
studentGpa = 1.8
if not (studentCredits >= 120) and not (studentGpa >= 2.0):
    print("You do not meet either requirement to graduate!")
elif not (studentCredits >= 120):
    print("Student doesn't have enough credit to graduate!")
elif not (studentGpa >= 2.0):
    print("Student's gpa isn't high enough to graduate!")
else:
    print("Student Can Graduate")
