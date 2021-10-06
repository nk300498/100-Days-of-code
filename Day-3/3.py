year = int(input("Which year do you want to check? "))

a=year%4
b=year%100
c=year%400
if b==0:
  if c==0:
    print(f"Year{ year} is leap year")
  else:
    print(f"Year { year} is not leapyear ")
elif a==0:
    print(f"Year { year} is leap year")
else:
    print(f"Year { year} is not leapyear ")


