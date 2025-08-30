secret_word = ['A','B','H','I','N','A','V']
secret_word_censor = ['*','*','*','*','*','*',"*"]
check = True
player_check = True

while check:
  if player_check:
    player_one_input = input("Player 1 - Enter\n1:Guess a character,\n2: guess the word")
    if player_one_input == '1':
      p1_c1 = input("Guess a character: ")
      found = False
      
      for i in range(len(secret_word)):
        if secret_word[i] == p1_c1:
          secret_word_censor[i] = p1_c1
          found = True
      if found:
        player_check = False
        print(''.join(secret_word_censor))
      elif not found:
        player_check = False
        print("Sorry. Your character is not in the word.")

    elif player_one_input == '2':
      found_2 = False
      p1_c2 = input("Guess the word: ")
      for i in range(len(p1_c2)):
        if p1_c2[i] != secret_word[i]:
          found_2 = True
      if found_2 == True:
        player_check = False
        print("Sorry. Your guess is not correct. Try again.")
        
      else:
        print("Congrats! You have gotten it correct!")
        check = False
  elif player_check == False:
    player_two_input = input("Player 2 - Enter\n1:Guess a character,\n2: guess the word")
    if player_two_input == '1':
      p1_c1 = input("Guess a character: ")
      found2 = False
      for i in range(len(secret_word)):
        if secret_word[i] == p1_c1:
          secret_word_censor[i] = p1_c1
          found2 = True
      if found2:
        player_check = True
        print(''.join(secret_word_censor))
      elif not found2:
        player_check = True
        print("Sorry. Your character is not in the word.")

    elif player_two_input == '2':
      found_3 = False
      p1_c2 = input("Guess the word: ")
      for i in range(len(p1_c2)):
        if p1_c2[i] != secret_word[i]:
          found_3 = True
      if found_3 == True:
        print("Sorry. Your guess is not correct. Try again.")
      else:
        print("Congrats! You have gotten it correct!")
        check = False
    
