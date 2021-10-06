print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L= ")
add_pepperoni = input("Do you want pepperoni? Y or N =")
extra_cheese = input("Do you want extra cheese? Y or N =")

if extra_cheese=="Y":
 if size=="S":
     if add_pepperoni=="Y":
          print(f"Your final bill is: ${18}")
     else:
          print(f"Your final bill is: ${16}")
 if size=="M":
      if add_pepperoni=="Y":
          print(f"Your final bill is: ${24}")
      else:
          print(f"Your final bill is: ${21}")

 if size=="L":
      if add_pepperoni=="Y":
          print(f"Your final bill is: ${29}")
      else:
          print(f"Your final bill is: ${26}")
else :
  if size=="S":
     if add_pepperoni=="Y":
          print(f"Your final bill is: ${17}")
     else:
          print(f"Your final bill is: ${15}")
  if size=="M":
      if add_pepperoni=="Y":
          print(f"Your final bill is: ${23}")
      else:
          print(f"Your final bill is: ${20}")

  if size=="L":
      if add_pepperoni=="Y":
          print(f"Your final bill is: ${28}")
      else:
          print(f"Your final bill is: ${25}")


