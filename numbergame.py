import random
playing=True
number=str(random.randint(10,20))

print("i will generate a number from 0 to 9, and you have to guess the number from one digit at a time")
print("the gameends when you get 1 hero!")

while playing:
    guess=input("Give me your best guess!\n")
    if number==guess:
        print("you win the game")
        print("the number was",number)
        break

    else:
        print("your guess isnt quite right, try again.\n" )