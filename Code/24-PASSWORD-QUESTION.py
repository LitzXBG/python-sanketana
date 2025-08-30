past_words = ["PopeyetheSailorm00n",
              "123qweasd",
              "Str0ngestpassw0rd"]

final = False
while final == False:
    alpha_chk = False
    num_chk = False
    len_chk = False
    previous_chk = False
    p1 = input("Enter new password: ")
    
        #alpha numeric
    for i in p1:
        if i.isalpha():
            alpha_chk = True
        elif i.isdigit():
            num_chk = True
        elif not i.isalnum():
            alpha_chk = False
            num_chk = False
            break
        # length
    if len(p1) >=8:
        len_chk = True
      #previoud check
    if p1 not in past_words:
        previous_chk = True


    if alpha_chk == False or num_chk == False:
        print("Password has to be alphanumeric.")
        continue
    if not len_chk:
        print("The password has to be at least 8 characters long.")
        continue
    if not previous_chk:
        print("This password already exists.")
        continue
    p2 = input("Re-Enter your password: ")
    if p2!=p1:
        print("The passwords don't match, Re enter your first password.")
        continue
    if (alpha_chk and num_chk and len_chk and previous_chk):
        print("Password set.")
        final = True
    
    
    
