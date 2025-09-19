# Task 4.1
import random

print("Welcome to NUMBERSTACK!")
while True:
  num_levels = int(input("Enter the number of levels to build (greater than 1): "))
  if num_levels <1:
    print("Enter more than 1 level please.")
    continue
  else:
    break
num_lst = ['0','1','2','3','4','5','6','7','8','9']


def add_level(tower):
  tower.insert(0,['-','-','-'])
  return tower



def fill_nums(empty_level_tower):
  global count
  count = 0
  lst = []
  num_before_lst = empty_level_tower[1]
  for i in num_before_lst:  
    empty_num = random.randint(int(i)-1,int(i)+1)
    empty_num = (empty_num + 10) % 10
    count+=1
    while int(empty_num) == int(i):
      empty_num = random.randint(int(i)-1,int(i)+1)
      empty_num = (empty_num + 10) % 10
      count+=1
      if int(empty_num) == 10:
        empty_num = 0
    lst.append(num_lst[empty_num])
    empty_level_tower[0] = lst


  return empty_level_tower
tower = [['0','0','0']]

print("Final tower: ")
for i in range(num_levels):
  add_level(tower)
  fill_nums(tower)
print(tower)
print("number of generated nos: ",count)

  

  

