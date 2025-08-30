# The following is the program code for Task 1

a = input("Enter the first position to occupy: ")
b = input("Enter the second position to occupy: ")

# Winning Combinations #
w1 = "123"
w2 = "456"
w3 = "789"
w4 = "147"
w5 = "258"
w6 = "369"
w7 = "159"
w8 = "357"


# Conditions for Win #
if a in w1 and b in w1:
    win = w1
elif a in w2 and b in w2:
    win = w2
elif a in w3 and b in w3:
    win = w3
elif a in w4 and b in w4:
    win = w4
elif a in w5 and b in w5:
    win = w5
elif a in w6 and b in w6:
    win = w6
elif a in w7 and b in w7:
    win = w7
elif a in w8 and b in w8:
    win = w8

for i in range(3):
    if win[i] != a and win[i] !=b:
        print(win[i])
    else:
        print("No specific position to block")

# Create new cells below and comment it as Task 1.1 for part 1
# Each answer should be answered in a new cell

# First copy the code from the previous cell, 
# paste it in the next cell, 
# then modify the code in the new cell.