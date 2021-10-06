print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")
#input()will get user input in console
input("What is your name?")
print("hello" + input("what is your name?"))

print(len(input("enter the string=")))

name=input("What is your name?")
l=len(name)
print(l)

a = input("a: ")
b = input("b: ")

c=a
a=b
b=c


print("a: " + a)
print("b: " + b)


#1. Create a greeting for your program.
print("welcome to band name generator")
#2. Ask the user for the city that they grew up in.
city=input("In which city you grew up?\n")
#3. Ask the user for the name of a pet.
pet_name=input("what is your pet name?\n")
#4. Combine the name of their city and pet and show them their band name.
print("Band Name="+ city + pet_name)
#5. Make sure the input cursor shows on a new line, see the example at: