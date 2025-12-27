#  write a program that generates a random number and asks the user to guess it
import random

randomNumber = random.randint(1 , 100)
userNumber = -1
guesses = 1

while(userNumber != randomNumber):
    userNumber = int(input("Guess a number:  "))
    if(userNumber > randomNumber):
        print("Guess a smaller number")
        guesses += 1 
    elif(userNumber < randomNumber):
        print("Guess a grater number")
        guesses += 1

print(f"You guessed {userNumber} correctly in {guesses} attempts")
