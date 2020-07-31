hours = int(input("Enter the hours: "))
minutes = int(input("Enter the minutes: "))
seconds = int(input("Enter the seconds:"))

if hours > 23 :
    print("your time is invlaid")
elif hours < 0 :
    print("your time is invalid")
elif minutes > 59 :
    print("your time is invalid")
elif minutes < 0 :
    print("your time is invalid")
elif seconds > 59 :
    print("your time is invalid")
elif seconds < 0 :
    print("your time is invalid")

else:
    print("your time is valid")
