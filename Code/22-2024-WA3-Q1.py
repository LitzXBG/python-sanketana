colours_allowed = ["blue", "red", "green", "grey", "orange"]
inv = {"shirt":["blue", "red", "green"],
 "flannel":["grey", "orange"]}
search = input("Input clothing to search for: ")
search = search.lower()
result = inv.get(search,"#")


if result == "#":
  enter = input("This does not exist, do you want to enter this? yes / no: ")
  enter = enter.lower()
  if enter == "yes":
    inv[search] = []
    while True:
      choice = input("Enter your colour: ").strip()
      if choice == "":
        break
      elif choice not in colours_allowed:
        print("Enter a colour that is allowed.")
        continue
      elif choice in inv[search]:
        print("You can only enter a colour once.")
        continue
      else:
        inv[search].append(choice)
        

      
else:
  print(result)
print(inv)


