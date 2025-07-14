name = ""
while name.strip(" ") == "":
    name = input("Please enter your name: ")
    print("Name cannot be empty, please re-enter")
print("Your name is",name)