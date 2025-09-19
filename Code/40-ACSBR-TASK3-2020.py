nlist = ["Alden", "Belle", "Charles", "Dolly", "Elle", "Falken", "Grace",
"Hacken"]
mlist = [56, 64, 23, 78, 53, 46, 98, 33] #error 1

to_find = input("Which name would you like to search for? ")
items = len(nlist) #error 4
num = 0
name_found = False

while name_found == True: #error 10
    while num < items: #error 7
        if nlist[num] == to_find: #error 2 and 3
            print("{} score {} for the test".format(nlist[num], mlist[num])) #error 6
            name_found = False #error 5
            num = items #error 8 
        elif num == items - 1:
            print("{} is not in the list".format(to_find))
            name_found = False
            num = items
        else:
            num+=1 #error 9