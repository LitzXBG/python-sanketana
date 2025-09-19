lst = []
while True:
  player1 = input("Player 1 enter a word: ")
  player1 = player1.lower()
  if not player1.isalpha():
    print("Cannot have numbers.")
    continue
  break
while True:
  player2 = input("Enter an anagram based on player 1s word: ")
  player2 = player2.lower()
  if not player2.isalpha():
    print("Cannot have numbers.")
    continue
  if len(player2) != len(player1):
    print("The 2 words must be the same length")
  break
for i in range(len(player2)):
  lst.append('X')



    