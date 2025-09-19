check = [2, 7, 6, 5, 4, 3, 2] #error 9
code = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "Z", "J"]  #error 1
total = 0
counter = 1 # error 8

NRIC = input("Enter the NRIC:")

while NRIC.isalnum() == False or len(NRIC) != 9: #Error 10
    if NRIC.isalnum() == False:
        print("Special character is not allowed!")
    else:
        print("NRIC must be 9 digits")  #error 2
    NRIC = input("Enter the NRIC again:")

while counter < len(NRIC) - 1:
    for digit in check:
        total += digit * int(NRIC[counter]) # error 3
        counter += 1 #error 4

remainder = total % 11 #error 5
subtract = 11- remainder  #error 7
if NRIC[7] == code[subtract - 1 ]: #error 6 
    print("The NRIC is valid.")
else:
    print("Invalid NRIC.")
