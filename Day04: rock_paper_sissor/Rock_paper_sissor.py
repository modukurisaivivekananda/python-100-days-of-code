c=input("what u want 0-rock 1-paper 2-sissor")
c=int(c)
import random
n=random.randint(0,2)
print(n)
if c==n:
  print("draw")
  exit()
elif n==1 and c==2:
  print("win")
  exit()
elif n==2 and c==0:
  print("win")
  exit()
elif n==0 and c==1:
  print("win")
  exit()
elif n==2 and c==1:
  print("loose")
  exit()
elif n==0 and c==2:
  print("loose")
  exit()
elif n==1 and c==0:
  print("loose")
  exit()
