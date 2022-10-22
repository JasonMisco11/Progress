import random
number = random.randint(1,10)

player_name = input("Hello, what is your name?: ")
number_of_guesses = 0
print(player_name+" I have a number between 1 and 10, can you guess it?")

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number :
        print("Your guess is too low. Try again :")
    if guess > number :
         print("Your guess is too high. Try again :")
    if guess == number :
        break
if guess == number :
        print("Your guessed the number in "+ str(number_of_guesses) + " tries!")
else:
        print("You did not guess the number, The number was " + str(number))
            