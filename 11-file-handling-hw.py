# 1. Write a program to create a file called students.txt and write the names of 5 students, each on a new line.
#    Then, read and print the names in reverse order.
#    Sample Input (students.txt):
#    Alice
#    Bob
#    Charlie
#    David
#    Eve
#    Sample Output:
#    Eve
#    David
#    Charlie
#    Bob
#    Alice
fw = open("students.txt","w")
fw.write("""
    Alice
    Bob
    Charlie
    David
    Eve
    Sample Output:
    Eve
    David
    Charlie
    Bob
    Alice""")
fw.close()


# 2. Given a file data.txt containing numbers (one per line), write a program to calculate and print the sum and average of all the numbers.
#    Sample Input (data.txt):
#    10
#    20
#    30
#    40
#    50
#    Sample Output:
#    Sum: 150
#    Average: 30.0

data = open("data.txt","w")
arr = []
number_of_numbers = int(input("Enter the number of numbers: "))
num = ""
for i in range(number_of_numbers):
    num = int(input("Enter the numbers: "))
    arr.append(num)

    
sum = 0
for j in arr:
    sum+=j
    data.write(str(j)+" "+"\n")
avg = sum/number_of_numbers
data.write("Sum: "+str(sum)+"\n")
data.write("Average: "+str(avg)+"\n")
data.close()

    



# 3. Write a program to copy the contents of one file (source.txt) to another file (destination.txt).
#    Sample Input (source.txt):
#    Hello, world!
#    This is a test file.
#    Sample Output (destination.txt):
#    Hello, world!
#    This is a test file.

source = open("source.txt","w")
inp = input("Enter anything: ")
source.write(inp)
destination = open("destination.txt","w")
destination.write(source.readlines())



# 4. Create a program that reads a file paragraph.txt and counts the number of words and sentences in the file.
#    Sample Input (paragraph.txt):
#    Python is fun. It is easy to learn!
#    Let's write some code.
#    Sample Output:
#    Number of words: 13
#    Number of sentences: 3

# 5. Write a program to remove all blank lines from a file called input.txt and save the result to a new file called output.txt.
#    Sample Input (input.txt):
#    Line 1
#
#    Line 2
#
#    Line 3
#    Sample Output (output.txt):
#    Line 1
#    Line 2
#    Line 3

# 6. Write a program that appends the current date and time to a file called log.txt every time the program is run.
#    Sample Input: (No input file needed; just run the program multiple times)
#    Sample Output (log.txt after two runs):
#    2024-06-01 14:30:00
#    2024-06-01 14:32:15

# 7. Given a file marks.txt where each line contains a student's name and their mark (e.g., Alice 85), write a program to find and print the name(s) of the student(s) with the highest mark.
#    Sample Input (marks.txt):
#    Alice 85
#    Bob 92
#    Charlie 78
#    David 92
#    Eve 88
#    Sample Output:
#    Bob
#    David

# 8. Write a program to read a file story.txt and replace every occurrence of the word "bad" with "good", saving the result to a new file edited_story.txt.
#    Sample Input (story.txt):
#    It was a bad day. The weather was bad.
#    Sample Output (edited_story.txt):
#    It was a good day. The weather was good.

# 9. Create a program that checks if a file called important.txt exists. If it does, print its contents; if not, create the file and write "This is an important file."
#    Sample Input: (If file exists, e.g., contains:)
#    Confidential information.
#    Sample Output:
#    Confidential information.
#    (If file does not exist:)
#    Sample Output (important.txt):
#    This is an important file.
#    Printed Output:
#    File created.

# 10. Write a program to read a file data.csv (comma-separated values), and print only the rows where the value in the second column is greater than 50.
#     Sample Input (data.csv):
#     Name,Score
#     Alice,45
#     Bob,67
#     Charlie,52
#     David,38
#     Eve,90
#     Sample Output:
#     Bob,67
#     Charlie,52
#     Eve,90