# Python String Slicing Practice Exercises

# Exercise 1: Reverse the Entire String
text = "PythonRocks"
# Task: Reverse the entire string using slicing.
print(text[-1::-1])


# Exercise 2: Extract "thon" using negative indexing
text = "PythonRocks"
# Task: Use only negative indexes to extract the substring "thon".
print(text[-9:-5])

# Exercise 3: Every 2nd character in reverse from end to start
text = "PythonRocks"
# Task: Print every second character in reverse.
print(text[::-2])


# Exercise 4: Extract "Rocks" using negative indexes
text = "PythonRocks"
# Task: Extract the last 5 characters using negative indexing.
print(text[-5::])

# Exercise 5: Reverse only the "Rocks" portion
text = "PythonRocks"
# Task: Use slicing to reverse just the word "Rocks".
print(text[:6]+text[-1:-6:-1])


# Exercise 6: Reverse "Python" using a negative step
text = "PythonRocks"
# Task: Reverse the first 6 characters using slicing with a negative step.
print(text[-6::-1]+text[6::])

# Exercise 7: Extract the middle 4 characters using positive and negative indexes
text = "PythonRocks"
# Task: Use a combination of positive and negative indexes to extract "honR".
print(text[3:7])
print(text[-8:-4])

# Exercise 8: Use negative slicing to get every alternate character of "Python"
text = "PythonRocks"
# Task: Use slicing with a step to extract every alternate character from "Python" using only negative indexing.
print(text[-6::-2])

# Exercise 9: Reverse only the word "Python" using slicing
text = "PythonRocks"
# Task: Use slicing to reverse only the first 6 characters.
print(text[5::-1]+text[6::])

# Exercise 10: Extract "tho" using a mix of positive and negative indexes
text = "PythonRocks"
# Task: Extract the substring "tho" using a combination of positive and negative indices.
print(text[2:5])
print(text[-9:-6])