for i in range(5):
    num_lst = []
    factor_count = 0
    
    number = int(input("Enter a number: "))
    for i in range(1, number + 1):
        if number % i == 0:
            factor_count += 1
            num_lst.append(i)
    print("The factors for "+str(number)+" is: ",num_lst)
