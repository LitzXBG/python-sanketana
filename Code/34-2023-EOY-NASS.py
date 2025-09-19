def rhyme_words(lst):

    if len(lst) < 2: #error 5
        print("The list should contain 2 or more words.")
        return None #error 4

    for word in lst:
        if len(word) < 2: #error 8
            print("The word", "\'"+word+"\'", "does not meet the requirement.")
            print("Words should have 2 or more letters.")
            return None #error 3

    #To check if the list contains all rhyme words
    check = True 

    for word in lst:
        if word[-2:] != lst[0][-2:]:
            check = False #error 7
            break

    #To find the root word among all rhyme words
    suffix = None

    if check == True: #error 1
        print("All the words in this list rhyme.")

        #Initialise a counter to track number of words in list
        #ending with suffix
        count = 0 #error 10

        while count != len(lst):

            #Loop iteration produces varying lengths of suffices
            for j in range(-1,-1*(len(lst[0])),-1):
                count += 1 #error 9
                suffix = lst[0][j:]

                #Loop checks if every word in list
 #contains suffix
                for i in range(len(lst)):
                    if lst[i].endswith(suffix): #error 6 
                        count += 1

                if count != len(lst):
                    if j != -1:
                        suffix = lst[0][j+1:]
                        print("The SUFFIX is", suffix)
                        count = len(lst)
                        continue
                    else:
                        suffix = None
                        count = len(lst)
                        continue


        print("The ending rhyme of every word is {}".format(suffix)) #error 2

        return suffix

    else:
        print("Not all the words in the list rhyme.")
        return suffix

