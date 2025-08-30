# # task 3.1 3.5 min
# def bowling_score(tv):
#   score = 0
#   for i in tv:
#     score+=int(i)
#   return score



# print(bowling_score("18181818181818181818"))


# def bowling_score_1(tv):
#   score = 0
#   for i in tv:
#     if i != '-':
#       score+=int(i)
      
#   return score

# print(bowling_score_1("128-5434221126718190"))

def bowling_score(tv):
  score = 0

  for i in range(0,len(tv)-2,2):
    if tv[i] == '>' and tv[i+1] == "<":
      score+=10
    elif tv[i+1] == '/':
      score+=10
   
    else:
      if tv[i] == '-':
        val_1 = 0
      else:
        val_1 = int(tv[i])
      if tv[i+1] == '-':
        val_2 = 0
      else:
        val_2 = int(tv[i+1])
      score+=(val_1+val_2)
      
  return score

print(bowling_score("><><><><><><><><><><><><><"))


