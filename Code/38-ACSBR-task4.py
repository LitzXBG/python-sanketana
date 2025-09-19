attendance = {"Monday":[],
              "Tuesday":[],
              "Wednesday":[],
              "Thursday":[],
              "Friday":[]}

for i in attendance:
  while True:
    student_attendance = input("Enter attendance for "+i+" : ")
    student_attendance = student_attendance.split(" ")
    is_invalid = False
    for j in student_attendance:
      if j not in ["P","A","E"]:
        print("Enter only P, A or E.")
        is_invalid = True
    if is_invalid:
      print("Invalid. Try again")
      continue
    else:
      attendance[i] = student_attendance
      break
total = 0
length = 0
for student_presence in attendance:
  count = 0
  for check in attendance[student_presence]:
    length = len(attendance[student_presence])
    if check == "P":
      count+=1
  total+=count
  print(student_presence,count,"student(s) are present")
print("Weekly attendance rate: ",(total/(length*5))*100,"%")
        

        
