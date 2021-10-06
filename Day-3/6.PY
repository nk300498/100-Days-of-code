print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

a1=(name1+name2).lower()
x1=a1.count("t")
x2=a1.count("r")
x3=a1.count("u")
x4=a1.count("e")
sum1=str(x1+x2+x3+x4)
x5=a1.count("l")
x6=a1.count("o")
x7=a1.count("v")
x8=a1.count("e")
sum2=str(x5+x6+x7+x8)

f=int(sum1 + sum2) 
if f<10 or f>90:
   print(f"Your score is {f}, you go together like coke and mentos.")
elif f>=40 and f<=50:
    print(f"Your score is {f}, you are alright together.")
else:
    print(f"Your score is {f}.")