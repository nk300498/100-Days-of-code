import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
print(names)
#print(random.choice(names))
a=(len(names)-1)
b=random.randint(0,a)
c=names[b]
print(c + " is going to buy the meal today")