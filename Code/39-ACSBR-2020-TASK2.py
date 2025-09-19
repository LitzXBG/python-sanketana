
upp_bound = 25
low_bound = 18.5
u_count = 0
o_count = 0
students = int(input("Enter the number of students youd like to enter: "))
for count in range(students):
    while True:
      weight = float(input("Enter weight of student in kg: "))
      if weight<=30 or weight>=150:
          print("Invalid weight")
          continue
      break
    while True:
      height = float(input("Enter height of student in cm: "))
      if height<=80 or height>=200:
          print("Invalid height")
          continue
      break
    bmi = weight / height**2 * 10000

    if bmi > upp_bound:
        print("Student is overweight")
        o_count+=1
    if bmi < low_bound:
        print("Student is underweight")
        u_count+=1
    if bmi>=low_bound and bmi<=upp_bound:
        print("Student's weight is normal")
print("The number of underweight students are",u_count)
print("The number of overweight students are",o_count)
