a=input("left or right")
a=a.lower()
if a=="right":
  print("you loose")
  exit()
elif a=="left":
  b=input("swim or wait")
  b=b.lower()
  if b=="swim":
    print("you loose")
    exit()
  elif b=="wait":
    c=input("which door to choose blue or green or yellow")
    c=c.lower()
    if c=="blue":
      print("you loose")
      exit()
    elif c=="green":
      print("you loose")
      exit()
    elif c=="yellow":
      print("you win")
      exit()
    else:
      print("invalid input")
      exit()
  else:
    print("invalid input")
    exit()
else:
  print("invalid input")
  exit()
