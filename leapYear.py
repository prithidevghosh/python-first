n= int(input("Enter the year"))
if n%400==0:
    print("leap year")
else:
    if n%100==0:
        print("not leap year")
    elif n%4==0:
        print("leap year")
    else:
        print("not leap year")