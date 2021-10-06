print("Welcome to the rollercoaster!")
height=int( input("Enter your height in cm="))
a=5
b=7
c=12


if height>=120:
    print("you can ride")
    age=int(input("enter your age="))
    if age<12:
       want_photo=input("want photo? Y or N=")
       if want_photo=="Y":
           t=a+3
           print(f"pay total ${t}")
       else:
           print(f"pay total ${a}")
    if 12<age<18:
       want_photo=input("want photo? Y or N=")
       if want_photo=="Y":
           t=b+3
           print(f"pay total ${t}")
       else:
           print(f"pay total ${b}")
    if age>18:
        want_photo=input("want photo? Y or N=")
        if want_photo=="Y":
            t=c+3
            print(f"pay total ${t}")
        else:
            print(f"pay total ${c}")
else:
  print("you can't ride")    

