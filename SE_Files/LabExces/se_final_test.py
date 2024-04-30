import pandas as pd
import numpy as np
import math

# Q1.mixed_list = ["hello", 2.0, 5*2, [10, 20],[3, 4, 6*6]]
# What's the length of the mixed_list?
mixed_list = ["hello", 2.0, 5 * 2, [10, 20], [3, 4, 6 * 6]]
len_mixed_list = len(mixed_list)
print(len_mixed_list)

# Question 2 (Mandatory) (2 points) 
# Given a dictionary called spec, where
# spec  = {"backend": "Mongodb", "frontend": "Angul
# Expected output:
# 1. Mongodb
# 2. {'backend':'mangodb','frontend':'AngularIS', 'App': 'website','App':'website'}
# 3.2. {'backend':'mangodb','App':'website'}


spec = {"backend": "Mangodb", "frontend": "AngularJS", "App": "website"}

modified_spec_dict = {}
for k in range(len(spec)):
    specified_key = list(spec.keys())[k]
    if specified_key in ["backend", "App"]:
        modified_spec_dict[specified_key] = spec[specified_key]

print("1. ", spec["backend"])
print("2. ", spec)
print("3. ", modified_spec_dict)


# Bmi Calculator Question
def bmi_status_identifier(user_bmi):
    if user_bmi < 18.5:
        return "Underweight"
    elif 18.5 <= user_bmi <= 24.9:
        return "Normal"
    else:
        return "Obese"


user_bmi = float(input("Please Enter your BMI: "))
print(f"Specified user BMI status is: {bmi_status_identifier(user_bmi)}")

# Question 3:
# create  a pandas dataframe . Include  product and price. Display the dataframe.
# Calculate the total price , average price of all the product . Display your output

kiana_product_box = {
    'Product': ['Laptop', 'Phone', 'Headphones', 'Tablet', 'Camera'],
    'Price': [1200, 800, 150, 500, 700]
}

# Question 4 - Pandas products Dataframe Question
kiana_product_dataframe = pd.DataFrame(kiana_product_box)
print("== Kiana's Products DataFrame: ==")
print(kiana_product_dataframe)
kiana_total_product_prices = kiana_product_dataframe['Price'].sum()
kiana_average_product_prices = kiana_product_dataframe['Price'].mean()

print("Total Product's Prices:", kiana_total_product_prices)
print("Average Prices Of The Products:", kiana_average_product_prices)

# Question 5 - Gross Income and Total Hourly Pay Calculator:
employee_hours_worked = float(input("Enter hours worked: "))
hourly_rate = float(input("Enter hourly rate: "))

gross_pay_calculator = employee_hours_worked * hourly_rate
net_pay = gross_pay_calculator * 0.8
print(f"Gross Pay: ${gross_pay_calculator}")
print(f"Net Pay: ${net_pay}")


def calculate_pay(hourly_wage, worked_hours):
    gross_pay = hourly_wage * worked_hours
    if worked_hours > 40:
        gross_pay = (hourly_wage * 40) + (1.5 * hourly_wage * (worked_hours - 40))
    net_pay = gross_pay - (gross_pay * 0.20)
    return gross_pay, net_pay


# Question 7 - Create a Shopping List Dict, then make some changes to it:
kiana_shopping_list = ["Apples", "Bananas", "Blueberries", "Rasberries", "Milk", "Eggs"]
print(kiana_shopping_list)

print("Shopping List:")
for item in range(len(kiana_shopping_list)):
    print(f"{item + 1}. {kiana_shopping_list[item]}")

print("\nItems 2 and 3:")
for index in [1, 2]:
    print(f"{index + 1}. {kiana_shopping_list[index]}")

kiana_shopping_list[3] = "Cheese"

print("\nUpdated Shopping List:")
for index in range(len(kiana_shopping_list)):
    print(f"{index + 1}. {kiana_shopping_list[index]}")

# Question 7 - Will Keep running until it recieves a negetive number:
while True:
    random_user_num = float(input("Pls input a random number "))

    if random_user_num < 0:
        print(f"U have iputed a negative number..\n killing the program")
        break

    print("The number u inputed was:", random_user_num)


# #Question 8
# Write a function that accepts a number from the user and uses
# a function to square the number and then return the result.
def square_root_generator(n):
    return n * n


user_input_number = float(input("Enter a number: "))
print(math.sqrt(user_input_number))
