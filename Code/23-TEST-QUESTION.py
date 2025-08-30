# NWA Revision Task 1
import random
colours = "RBGYO"
colours_lst = ["R","G","B","Y","O"]
correct = ""
count = 0
def generate_secret_code():
  
  rand_lst = []
  rand_dict = {"R":0,"G":0,"B":0,"Y":0,"O":0}
  while len(rand_lst)<4:
    rand_num = random.randint(0,4)
    if rand_dict[colours_lst[rand_num]] == 0:
      rand_lst.append(colours_lst[rand_num])
      rand_dict[colours_lst[rand_num]] +=1
  return ''.join(rand_lst)
  
secret_code = generate_secret_code()

while count<=8:
  guess = input("Enter your 4 letter guess: ")
  count+=1
  guess = guess.upper()
  if len(guess) != 4:
    print("Enter 4 letters only.")
    continue
  for i in guess:
    if i not in colours_lst:
      print("Please enter letters in RBGYO.")
  else:
    for i in range(len(guess)):
      if guess[i] == secret_code[i]:
        correct+="B"
      elif guess[i] in secret_code:
        correct+="W"
      elif guess[i] not in secret_code:
        correct+="X"
      elif guess == secret_code:
        break


  print("Your word: "+guess+"\n"+correct+"\n"+secret_code)
print("the code is ",secret_code)

    

  

  


