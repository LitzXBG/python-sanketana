try:   
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    if num1<0 or num2<0:
        raise Exception("Negative number error.")
    
    print(num1/num2)
except ZeroDivisionError:
    print("Error cannot divide by 0")
except ValueError:
    print("Error cannot divide by alphabet")
except Exception as e:
    print("Error occured", e)
    print(type(e))
    print(dir(e))
    print(str(e))
    print("Exception type: ",type(e).__name__)
    print("Exception message: ",str(e))
    


#ZeroDivisionError: division by zero                                                                 
#ValueError
                                                                                                           