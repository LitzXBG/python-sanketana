
def check_space(word):
  if ' ' in word:
    return True
  False

while True:
  firstname = input("Please enter your first name: ")
  if check_space(firstname) == True or len(firstname) <3:
    print("your name cannot have a space inside and has to be longer than 3 words.")
    break
  lastname = input("Please enter your last name: ")

  username = firstname[0:3] + lastname[0:3]
  username = username.upper()


  print("Your username is {}".format(username))
  pin = int(input("Please enter a PIN: "))
  if len(str(pin)) != 6:
    print("pin can only be 6 digits.")
    continue
  pin2 = int(input("Please re-enter your pin: "))
  if pin2!=pin:
    print("Pin entries do not match. Please repeat.")
    continue
  
  else:
    print("pin set.")
    break
