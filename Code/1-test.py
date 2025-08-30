def staircase(lvl):
    # your code here # 
    rows = []
    if lvl>0:
        for i in range(1,lvl+1):
            
            rows.append("_"*(lvl-i)+"#"*i)
    elif lvl<0:
        for i in range(0,abs(lvl)):
            
            rows.append("_"*(i)+"#"*(abs(lvl)-i))
    return "\n".join(rows)



print(staircase(-8))