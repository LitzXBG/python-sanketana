def shadow_check(s1, s2):
  if len(s1) != len(s2): #error 2
    return "Invalid. Both sentences must have same lengths."
  else: # error 1
    for i in range(len(s1)): # error 4
      if s1[i] in s2: #error 3
        if s1[i] != " ":
          return "Same characters found. Not shadow sentences."
    return "Both are shadow sentences."