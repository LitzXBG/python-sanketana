num_user = 4
age_limit = 18
below_age_limit = 0
meet_age_limit = []
total_age = 0
oldest = 0
count = 0
age =""
while True:
  age = input("Enter the age of user: ")
  if age.isdigit() == False:
    print("Enter a valid age which is made of integers.")
    continue
  
  elif int(age) > age_limit:
    print("The user is of age.")
    meet_age_limit.append(age)
  elif int(age)<0:
    print("Enter a valid age that is positive")
    continue
  else:
    print("The user is below required age limit.")
    below_age_limit+=1
    if (len(meet_age_limit)+below_age_limit) == num_user:
      break
    continue
print("Users below age limit are, ",below_age_limit)
print("The number of users who have met the age limit: ",len(meet_age_limit))
for i in meet_age_limit:
  total_age+=int(i)
  if int(i) > age:
    oldest = i
print("average age is ",total_age/len(meet_age_limit))
print("The oldest person is ",oldest,"years old")



