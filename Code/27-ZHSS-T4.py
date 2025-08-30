import math
def get_quotes(weight,price,est_weight):
  diff = est_weight/weight
  price = price*math.ceil(diff)
  return price

lst = []
while True:
  no_companies = int(input("Enter the number of mover companies: "))
  try:
    X_val = int(input("Enter all the X values: "))
    for i in range (no_companies):
      lst.append(X_val)
  except ValueError:
    print("Enter an integer.")
    continue
    