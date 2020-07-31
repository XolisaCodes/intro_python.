n = int(input("Enter the start point: "))
m = int(input("Enter the end point: "))

for i in range(n, m):
  y = True
  if(str(i) == str(i)[::-1 ]):
    if(i>2):
      for n in range(2,i):
         if(i%n==0):
           y = False
           break
    if(y):
      print(i)
