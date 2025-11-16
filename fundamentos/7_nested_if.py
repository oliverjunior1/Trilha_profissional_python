age = int(input("Put your age:"))
has_license = int(input("If has license put 1 else don't have put 2: "))

if age>=18:
    if has_license==1:
        print("You can drive")
    else:
        print("You can't drive")
else:
    print("You're too young to drive!")