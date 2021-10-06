print("welcome to tip calculator\n")
b=float(input("what was the total bill?$\n"))
t=float(input("what % tip would you like to give?"))

t2=int(input("How many of you?\n"))
b1=(b/t2)*((t+100)/100)
c="{:.2f}".format(b1)
print(c)