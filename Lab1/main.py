# Question 1
# a = [10, 20, 30, 20, 40, 50]
# Remove the first occurance of 20

a = [10, 20, 30, 20, 40, 50]
a.remove(20)
print("After removing first occurance of 20: ", a)

# ==============================================================================================

# Question 2
# Remove element at index 1 and return its value in val

a = [10, 20, 30, 40, 50, 60, 70]
val=a.pop(1)
print("After removing element at index 1: ", a)

# ==============================================================================================

# Question 3
# Removes elements from index 1 to index 3 (which are 20, 30, 40)

a=[10, 20, 30, 40, 50, 60, 70]
a[1:4]=[]
print("After removing elements from index 1 to 3: ", a)

# ==============================================================================================

# Question 4
# Remove all elements

a=[10, 20, 30, 40, 50, 60, 70]
a.clear()
print("After removing all elements: ", a)


# ==============================================================================================

# Question 5
# Write a program that prints the number of times the substring 'iti' occurs in a string

string="this is iti iti"
print(string.count("iti"))

# ==============================================================================================

# Question 6
# application to take a number in binary form from the user, and print it as a decimal

num=input("Enter a binary number: ")
print(int(num,2))

# ==============================================================================================

# Question 7
# write a code take a number as an argument and if the number divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is divisible by both return "FizzBuzz"

num = int(input("Enter a number: "))
if num % 3 ==0 and num % 5 ==0:
    print("FizzBuzz")
elif num % 3 ==0:
    print("Fizz")
elif num % 5 ==0:
    print("Buzz")
else:
    print(num)


# ==============================================================================================

# Question 8
# Ask the user to enter the radius of a circle print its calculated area and circumference

print("Enter the radius of a circle: ")
radius = float(input())
area= round(3.14 * radius * radius, 3)
circumference = round(2 * 3.14 * radius, 2)
print(f"Area: {area} Circumference: {circumference}")

# ==============================================================================================

# Question 9
# Ask the user for his name then confirm that he has entered his name (not an empty string/integers).then proceed to ask him for his email and print all this data

while True:
    name = input("Enter your name: ").strip()
    if name.isalpha():
        break
    else:
        print("Please enter a valid name")
print("Enter your email: ")
email = input()
print(f"Name: {name} Email: {email}")

# ==============================================================================================
