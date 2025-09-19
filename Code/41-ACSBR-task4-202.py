employee_lst = []
time_worked_lst = []
total = 0
for i in range(2):
  temp_staff = input("Enter temporary staff name: ")
  employee_lst.append(temp_staff)
  check = False
  while True:
    time_in = input("Time-in HH:MM for "+temp_staff+" : ")
    time_in = time_in.replace(" ","")
    if len(time_in) != 5:
      print("Invalid!")
      continue
    
    elif time_in[2] != ":":
      print("Invalid!")
      continue
    
    elif int(time_in[:2]) >23 or  int(time_in[:2]) < 0:
      print("Invalid!")
      continue
    
    elif int(time_in[3:]) >59 or  int(time_in[3:]) < 0:
      print("Invalid!")
      continue
    else:
      while True:
        time_out = input("Time-out HH:MM for "+temp_staff+" : ")
        time_out = time_out.replace(" ","")
        if len(time_out) != 5:
          print("Invalid!")
          continue
        
        elif time_out[2] != ":":
          print("Invalid!")
          continue
        
        elif int(time_out[:2]) >23 or  int(time_out[:2]) < 0:
          print("Invalid!")
          continue
        
        elif int(time_out[3:]) >59 or  int(time_out[3:]) < 0:
          print("Invalid!")
          continue
        elif int(time_out[:2]) < int(time_in[0:2]):
          print("Invalid!")
          continue
        else:
          time_work = (int(time_out[:2]) - int(time_in[0:2]))*60 + (int(time_out[3:])-int(time_in[3:]))
          time_worked_lst.append(time_work)
          break
    break

    
for i in range(len(employee_lst)):
  print(employee_lst[i]+" worked for "+str(time_worked_lst[i])+" minutes")
for i in time_worked_lst:

  total+=int(i)
print("Average number of minutes worked: "+str((total/len(time_worked_lst))))


