start= int(input("Enter the start number: "))

if -6 < start and start < 2:
    for x in range(start, 38 - (start < -4), 7):
        for y in range(x,  x + 7):
            print("{0:2}".format(y), end=" ")
        print()
