#number guessing  game in Python 3

#system will generate a random number between 1 and 100
import random
print("Welcome to the number guessing game!")
print("I have selected a random number and you have to guess it.")
print("You have 10 chances to guess the number.")

print("set boundaries for the random number")
lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

print(f"Guess a number between {lower_bound} and {upper_bound}")

#generate a random number between lower_bound and upper_bound
random_number = random.randint(lower_bound, upper_bound)

#initialize the number of chances
chances = 10
#initialize the number of guesses counter
gueess = 0 

while gueess < chances:
    gueess += 1
    guess_number = int(input("enter your guess: "))

    if guess_number == random_number:
        print(f"Congratulations! You guessed the number {random_number} correctly in {gueess} tries.")
        
        break
    # elif guess >= chances and guess != random_number:
    #     print(f'orry! The number was {random_number}. Better luck next time.')
    elif guess_number < random_number:
        print("Your guess is too low. Try again.")
    elif guess_number > random_number:
        print("Your guess is too high. Try again.")
    else:
        print("Invalid input. Please enter a number between the specified bounds.")

    

