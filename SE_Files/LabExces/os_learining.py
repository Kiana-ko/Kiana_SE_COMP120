import os

# An assignment which involves experimenting with OS

"""
Exercise 3
using OS Module , explore the following functions  and execute the command
1. Write a command to create a new directory using OS Library
2. Write a command to delete the existing file
"""

if not os.path.exists("new_os_directory"):
    try:
        os.makedirs("new_os_directory")
    except FileExistsError:
        print("Directory already exists")
    else:
        print("New directory created successfully")
else:
    print("Directory already exists")

print(os.listdir())

try:
    os.rmdir("new_os_directory")
except FileNotFoundError:
    print("File not found")