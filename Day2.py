two_digit_number = input("Type a two digit number: ")

a1=two_digit_number[0]
a2=two_digit_number[1]
a3=int(a1)
a4=int(a2)
print(a3+a4)


height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

h=float(height)
w=float(weight)
BMI=(w/(h*h))
#a=int(BMI)
print(BMI)


age = input("What is your current age?\n")
a=int(age)
b=90-a
d=b*365
w=b*52
m=b*12
print(f"you have {d} days,{w} weeks and {m} months left")


print("welcome to tip calculator\n")
b=float(input("what was the total bill?\n$"))
t=float(input("what % tip would you like to give?\n"))

t2=int(input("How many of you?\n"))
b1=(b/t2)*((t+100)/100)
c="{:.2f}".format(b1)
print(f"every one pay ${c}")