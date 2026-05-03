import random

secret = random.randint(1, 100)
attempts = 0
print("Guess the number between 1 and 100!")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {secret} in {attempts} attempts!")

        print("Do you want to play again? (y/n)")
        play_again = input().lower()
        if play_again == "y":
            secret = random.randint(1, 100)
            attempts = 0
            print("Guess the number between 1 and 100!")
        else:
            print("Thanks for playing! Goodbye!")
            break
