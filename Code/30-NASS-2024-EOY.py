userbase = {
    "Name":['Gender','Personality','hobby'],
    "Alice": ["Female", "Extroverted", "travel"],
    "Bob": ["Male", "Introverted", "coding"],
    "Carol": ["Female", "Extroverted", "photography"],
    "David": ["Male", "Introverted", "coding"],
    "Emily": ["Female", "Extroverted", "travel"],
    "Frank": ["Male", "Kind", "volunteering"],
    "Grace": ["Female", "Curious", "reading"],
    "Henry": ["Male", "Kind", "music"],
    "Ivy": ["Female", "Curious", "reading"],
    "John": ["Male", "Curious", "travel"]
}
userbase1 =  {
    "Alice": ["Female", "Extroverted", "travel"],
    "Bob": ["Male", "Introverted", "coding"],
    "Carol": ["Female", "Extroverted", "photography"],
    "David": ["Male", "Introverted", "coding"],
    "Emily": ["Female", "Extroverted", "travel"],
    "Frank": ["Male", "Kind", "volunteering"],
    "Grace": ["Female", "Curious", "reading"],
    "Henry": ["Male", "Kind", "music"],
    "Ivy": ["Female", "Curious", "reading"],
    "John": ["Male", "Curious", "travel"]
}

#task 1.1
name = input("Please enter the name of a user: ")
if name in userbase:
  print(name,"'s profile is: ",userbase[name])
else:
    add = input("Would you like to add a new entry? (Y/N): ")
    add = add.upper()
    if add == "Y":
        gender = input("Enter gender: ")
        personality = input("Enter personality: ")
        hobby = input("Enter hobby: ")
        lst = [gender,personality,hobby]
        userbase[name] = lst
        print(userbase)

personality_dict = {"Extroverted":[],"Introverted":[],"Kind":[],"Curious":[]}
for i in userbase1:
    personality1 = userbase1[i][1]
    temp = personality_dict[personality1]
    temp.append(i)
    personality_dict[personality1] = temp

personality_type = input("Enter the personality type: ")
print(personality_dict[personality_type]," should be friends as they are all "+personality_type)

