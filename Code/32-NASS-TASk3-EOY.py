# Task 3

word_lst = []

for i in range(26):
    word = word_lst.append([])

letters = 'abcdefghijklmnopqrstuvwxyz'

no_games = input("Enter number of games to compete: ")

win_lst = [0,0]  #stores number of wins for P1 and P2

for n in range(int(no_games)): #error 3

    print("\n###############")
    print("Game", n+1)
    print("###############")
    
    import random
    rand_no = random.randint(0,25) # error 10
    rand_letter = letters[rand_no]

    print("The letter chosen for this round is", rand_letter)
    print("All words entered must start with this letter.")

    win = False # error 1
    player_no = 1

    while win == False:
        print("Player " + str(player_no) + "'s turn") #error 4
        word = input("Enter a word starting with letter " + rand_letter + " : ")
        word = word.lower() # error 2

        if word in word_lst[rand_no]:
            print("The word you have entered has already been used previously.")
            print("Player", player_no, "lose.")
            win = True
            win_lst[player_no-1] += 1 #error 8
            
        elif word.startswith(rand_letter) == False: #error 5
            print("Word must begin with", rand_letter)
            print("Player", player_no, "lose.")
            win = True
            win_lst[player_no-1] += 1 #error 9
            
        else:
            word_lst[rand_no] += [word]
            print("Good try. Word has been added")
            if player_no == 1:
                player_no = 2 #error 6
            else:
                player_no = 1 # error 7 
        
if win_lst[0] > win_lst[1]:
    print("Player 1 is the overall winner out of", no_games, "games.")
elif win_lst[0] < win_lst[1]:
    print("Player 2 is the overall winner out of", no_games, "games.")
else:
    print("It is a draw out of", no_games, "games.")

print("\nList of all words entered by users.")

for lst in word_lst:
    if lst != "":
        print(lst)
