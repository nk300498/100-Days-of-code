import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rpc=[rock,paper,scissors]

a=random.randint(0,2)
b=rpc[a]

c=(input("Enter Rock,Paper,Scissors=\n")).lower()
if c=="rock":
     print("You selected Rock"+rpc[0])
     c1=0
elif c=="paper":
     print("You selected Paper"+rpc[1])
     c1=1
elif c=="scissors":
     print("You selected Scissors"+rpc[2])
     c1=2
else:
    print("plz check your spelling\n")

print("Computer selected"+rpc[a])
if a==c1:
    print("Game tied")
elif a==0 and c1==1:
    print("You win")
elif a==1 and c1==0:
    print("You lose")
elif a==0 and c1==2:
    print("You lose")
elif a==2 and c1==0:
    print("You win")
elif a==1 and c1==2:
    print("You win")
else: 
    print("You lose")
