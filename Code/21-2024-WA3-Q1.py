colours_allowed = ["blue", "red", "green", "grey", "orange"]
inv = {"shirt":["blue", "red", "green"],
 "flannel":["grey", "orange"]}
search = input("Input clothing to search for: ")
search = search.lower()
check = True
col_dict = {"blue":0,
              "red":0,
              "green":0,
              "grey":0,
              "orange":0}
while True:
  if search == "shirt":
    print(inv["shirt"])
    break
  elif search == "flannel":
    print(inv["flannel"])
    break
  else:
    add = input("do you want to add another item? Yes/No")
    if add == "yes":
      choice = input("Enter the item name: ")
      inv[choice] = []
      while check:
        colour = input("Enter your colour: ")
        colour = colour.lower()
        if colour=="":
          break
        if colour not in colours_allowed:
          print("Please enter appropriate colours: ")
          continue
        
        col_dict[colour]+=1
        inv[choice].append(colour)
        
        if col_dict[colour]>1:
          print("Please enter each colour 1 time only.")
          continue

      break
    else:
      print("the item you are looking for doesn't exist.")
      break
  
  
