import random
CARDS = []
lst1 = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
lst2 = ["D","H","C","S"]
point = 0
for i in lst1:
  for j in lst2:
    CARDS.append(i+j)

shuffled_lst = []
random_lst = []
def deal():

  while len(shuffled_lst) != 52:
    random_index = random.randint(0,len(CARDS)-1)
    
    if random_index not in random_lst:
      shuffled_lst.append(CARDS[random_index])
      random_lst.append(random_index)
      
  return shuffled_lst
def points():
  mid = len(deal())//2
  p1 = deal()[:mid]
  p2 = deal()[mid:]



points()


