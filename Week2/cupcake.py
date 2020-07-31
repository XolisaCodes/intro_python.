print("Welcome to the 30 second rule expert.Please Answer either yes/no")
r = input("Did anyone see you? yes/no ")
if r == 'no' :
    r = input("Was it sticky? yes/no ")
    if r == 'no' :
        r = input("Is it an Emausaurus? yes/no ")
        if r == 'no' :
            r = input("Did the cat lick it? yes/no ")
            if r == 'no' :
                decision = "EAT IT"
                print(decision)
            else:
                r = input("Is your cat healthy? ")
                if r == 'no' :
                    decision = 'YOUR CALL'
                    print(decision)
                else:
                    decision = 'EAT IT.'
                    print(decision)
        else:
            r = input("Are you a Megalosaurus? yes/no")
            if r == "no" :
                decision = 'DONT EAT IT'
                print(decision)
            else:
                decision = 'EAT IT.'
                print(decision)
    else:
        r = input("Is it a raw steak? yes/no ")
        if r == 'no' :
            r = input("Did the cat lick it? yes/no ")
            if r == 'no' :
                decision = "EAT IT."
                print(decision)
            else:
                r = input("Is your cat healthy? yes/no ")
                if r == 'no' :
                    decision = 'YOUR CALL'
                    print(decision)
                else:
                    decision = 'EAT IT'
                    print(decision)
        else:
            r = ("Are you a puma? yes/no ")
            if r == 'no' :
                decision = 'DONT EAT IT'
                print(decision)
            else:
                decision = 'EAT IT'
                print(decision)

else:
    r = input("Was it a boss/lover/parent? yes/no ")
    if r == 'no' :
        decision = 'EAT IT'
        print(decision)
    else:
        r = input("Was it expensive? yes/no ")
        if r == 'no' :
            r = input("Is it chocolate? yes/no ")
            if r == 'no' :
                decision = 'DONT EAT IT.'
                print(decision)
            else:
                decision = 'EAT IT.'
                print(decision)
        else:
            r = input("Can you cut off th part that touched the floor? yes/no")
            if r == 'no' :
                decision = 'YOUR CALL'
                print(decision)
            else:
                decision = 'EAT IT'
                print(decision)
