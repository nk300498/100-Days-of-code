#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
a=random.choice(word_list)
print(a)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
b=input("Guess a Latter=").lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for i in a:
    print(i)
    if i==b:
        print("True")
    else:
        print("False")