choice = input("Press B for conversion to Binary and D for conversionto Denary: ") 
choice = choice.upper()
while (choice != 'D' or choice != 'B'): #error 1
    print("Wrong input.")
    choice = input("Press B for conversion to Binary and D for conversion to Denary: ")
    choice = choice.upper()

if choice == "D":
    denary = input("Enter denary number: ")
    denary = int(denary)  #error 2
    binary = ""
    while True:
        r = denary % 2
        binary += str(r)
        denary = denary % 2
        if denary == 0:
            break #error 7
        print("The binary number is:", binary[::]) #error 3

elif choice == "B": #error 5
    denary = 0
    binary = input("Enter binary number: ") #error 6
    binary = binary[::-1]
    for n in range(len(binary)): #error 4
        denary += int(binary[n]) * 2 * n  
print("The denary number is:", denary)
