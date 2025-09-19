def length(x1,y1,x2,y2):
  line = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
  return line

def gradient(x1,y1,x2,y2):
  return (y1-y2)/(x1-x2)

def c(x1,y1,x2,y2):
  return y1-(gradient(x1,x2,y1,y2)*x1)

def validate(c):
  while True:
    coord = int(input("Enter "+c+":"))
    if coord < -10 or coord > 10:
      print("number should be between -10.0 to 10.0 only")
      continue
    return coord

x1 = validate('x1')
y1 = validate('y1')
x2 = validate('x2')
y2 = validate('y2')
if (x1 == x2) and (y1 == y2):
  print("the 2 pairs of coordinates are the same point.")
elif (x1-x2) == 0:
  print("Both sets of coordinates form a vertical line.")
  print("The equation of the line is x = ",(y1-y2))
elif (y1-y2) == 0:
  print("Both sets of coordinates form a horizontal line.")
  print("The equation of the line is y = ",(x1-x2))
else:
  print("Both sets of coordinates form a diagonal line.")
  print("The equation of the line is y = "+str(gradient(x1,y1,x2,y2))+"x + "+str(c(x1,y1,x2,y2)))