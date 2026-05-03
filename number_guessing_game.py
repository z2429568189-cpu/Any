import random

secret = random.randint(1, 100)
attempts = 0
score = 0
print("Guess the number between 1 and 100! (Type 'q' to quit)")

while True:
    guess_input = input("Enter your guess: ").strip().lower()
    if guess_input in ("q", "quit"):
        print(f"Thanks for playing! Final total score: {score}")
        break
    try:
        guess = int(guess_input)
    except ValueError:
        print("Please enter a valid integer or 'q' to quit.")
        continue
    attempts += 1
    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        points = max(1, 11 - attempts)
        score += points
        print(f"Congratulations! You've guessed the number {secret} in {attempts} attempts!")
        print(f"You earned {points} points! Total score: {score}")
        print("Do you want to play again? (y/n)")
        play_again = input().strip().lower()
        if play_again == "y":
            secret = random.randint(1, 100)
            attempts = 0
            print("Guess the number between 1 and 100! (Type 'q' to quit)")
        else:
            print(f"Thanks for playing! Final total score: {score}")
            break
