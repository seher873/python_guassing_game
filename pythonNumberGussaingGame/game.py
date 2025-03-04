import random

print("wellcome to the game","this is a guessing game","you have 5 attempts to guess the number between 50 to 100","let's start the game")

number_to_guess:int=random.randrange(50,100)
chances:int=5

guass_counter:int=0

while guass_counter<chances:
    guass_counter=++1
    my_guass=int(input("inter your number:"))
    if my_guass ==number_to_guess:
        print(f"the number is correct{number_to_guess}and you found in right!!{number_to_guess} attempts") 
    elif guass_counter >= chances and my_guass!=number_to_guess:
        print(f"oops! sorry, your number is{number_to_guess}better luck next time")
        
    elif my_guass < number_to_guess:
     print("your number is too low")
    elif my_guass >number_to_guess:
     print("your number is too high")
    elif my_guass>number_to_guess:
     print("your number is too high,try again")
















    