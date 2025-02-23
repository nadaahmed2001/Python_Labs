# Question 1 :
# Write a simple calculator program using match to perform addition, subtraction, multiplication, and division.
# operation = "add"
# a, b = 10, 5
# # Expected Output: 15

def calculator(operation,a,b):
    match operation:
        case "add":
            print(a+b)
        case "sub":
            print(a-b)
        case "mul":
            print(a*b)
        case "div":
            print(a/b)
        case _:
            print("Invalid operation")

print("---------------- Question 1 ----------------")
calculator("add",10,5)
calculator("sub",10,5)

# =====================================================================================
# Question 2 :
# Write a program to filter out even numbers from a list and count how many are left.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # Expected Output: [1, 3, 5, 7, 9], Count = 5

def filter_even(nums):
    filtered_list=[num for num in nums if num%2!=0]
    print(filtered_list)
    print("Count of odd numbers: ",len(filtered_list))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("---------------- Question 2 ----------------")
filter_even(numbers)



# =====================================================================================
# Question 3 :
# Write a program to check if a password meets the following criteria:
# - At least 8 characters long.
# - Contains at least one uppercase letter.
# - Contains at least one digit.
# password = "Pass1234"
# # Expected Output: "Valid Password"

def check_password(password):
    if  len(password)>=8 and any(char.isupper() for char in password) and any(char.isdigit() for char in password):
        print("Valid Password")
    else:
        print("Invalid Password")
    
password = "Pass1234"
print("---------------- Question 3 ----------------")
check_password(password)

# =====================================================================================
# Question 4: 
# Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


def concatenate_dicts(*dicts):
    new_dict={}
    for d in dicts:
        new_dict.update(d)
    print(new_dict)

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
print("---------------- Question 4 ----------------")
print("Concatenated dictionary: ")
concatenate_dicts(dic1,dic2,dic3)

# ======================================================================================
# Question 5: 
# takes a string and prints the longest
# alphabetical ordered substring occured.
# For example, if the string is 'abdulrahman' then the output is:
# Longest substring in alphabetical order is: abdu

def longest_substring(s):
    longest_substring = s[0]
    current_substring = s[0]
    for i in range(1,len(s)):
        if s[i] >= s[i-1]:
            current_substring += s[i]
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring
        else:
            current_substring = s[i]
    print("Longest substring in alphabetical order is: ",longest_substring)

s = 'abdulrahman'
print("---------------- Question 5 ----------------")
longest_substring(s)
# ======================================================================================
# Question 6:
# Write a program to check if a Email meets the following criteria:
# - Ensures the email follows a standard format (e.g., local@domain.com).
# - Does not check if the email actually exists or is deliverable.

import re
def check_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(pattern,email):
        print("Valid Email")
    else:
        print("Invalid Email")

email = "local@domain.com"
print("---------------- Question 6 ----------------")
check_email(email)
# ======================================================================================
