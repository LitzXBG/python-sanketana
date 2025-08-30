# 1️⃣ Divide Two Numbers (with Zero Division Handling)
# Write a program that takes two numbers as input and prints the result of their division. Use try-except-else-finally to handle division by zero.

# 📥 Sample Input:
# Enter numerator: 10
# Enter denominator: 2

# 📤 Sample Output:
# Result: 5.0
# Division successful.
# Program completed.
try:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    print("Result: ",num1/num2)
    print("Programme complete")
except ZeroDivisionError:
    print("Error cannot divide by 0")
# ⸻

# 2️⃣ File Reading with Exception Handling
# Write a program that asks for a filename and tries to open and read it. Handle FileNotFoundError and use finally to print “Done reading attempt.”
try:
    file_name = input("Enter the file name: ")
    fil = open(file_name,"r")
    fil.readlines()

except FileNotFoundError:
    print("No such file exists")
finally:
    print("Done readng attempt.")
    fil.close()



# 📥 Sample Input:
# Enter filename: notes.txt

# 📤 Sample Output:
# File not found.
# Done reading attempt.

# ⸻

# 3️⃣ Age Input with Type Checking
# Ask the user to enter their age. Catch ValueError if the input is not an integer. Use else to confirm valid age input.
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Enter an integer: ")
else:
    print("your age is: ",age)


# 📥 Sample Input:
# Enter your age: twenty

# 📤 Sample Output:
# Invalid input. Please enter a number.

# 📥 Sample Input:
# Enter your age: 25

# 📤 Sample Output:
# Your age is 25.

# ⸻

# 4️⃣ Dictionary Key Access with Exception Handling
# Write a program that asks for a key and tries to access a value from a dictionary. Handle KeyError and always print “Operation complete” using finally.
try:
    key = input("Enter the key: ")
    d = {"name": "Alex", "age": 14, "grade": "A"}
    d[key]
except KeyError:
    print("It doesnt exist.")
finally:
    print("Operation completed")

# 📥 Sample Input:
# Enter key to look up: email

# 📤 Sample Output:
# Key not found.
# Operation complete.

# ⸻

# 5️⃣ Square Root Calculator (Custom Negative Check)
# Ask the user to enter a number and print its square root. Raise a ValueError if the number is negative. Use try-except-else-finally.
try:
    num = int(input("Enter a number: "))
    if num<0:
        raise ValueError
except ValueError:
    print("its a negative number")
else:
    print("The square root is: ",num**.5)
finally:
    print("calculation done.")
# 📥 Sample Input:
# Enter a number: -4

# 📤 Sample Output:
# Cannot calculate square root of a negative number.
# Calculation attempt done.

# 📥 Sample Input:
# Enter a number: 9

# 📤 Sample Output:
# Square root is 3.0
# Calculation attempt done.