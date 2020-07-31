num = int(input("Enter the start number :"))

if num > -6 and num < 93 :
  for i in range(num, num + 7):
    if i % 1 == 0:
      print("{0:2}".format(str("")), i, end="")
else:
  print("The number must be between -6 and 93! ")
