import random

def play_game():
    
    lower_limit = 1
    upper_limit = 100
    maxattempts = 10
    secret_number = random.randint(lower_limit, upper_limit)
    attempts = 0
    won = False
    print("Welcome, to the game where you have to guess the number which i am thinking")
    print("Guess the number between", lower_limit,"and", upper_limit)
    print("you have", maxattempts, "attempts")

    while attempts < maxattempts:
        try:
            guess = int(input("Enter your number: "))
            
            if not (lower_limit <= guess <= upper_limit):
                    print("Invalid input. Please enter a number within the specified range ({lower_limit}-{upper_limit}).")
                    continue
            attempts =+ 1

            if guess == secret_number:
                print("Congratulations, Your guess was correct")
                won = True
                break
            if guess < secret_number:
                print("guess was low, try something greater")
            if guess > secret_number:
                print("guess was high, guess something lower")
        
        except ValueError:
                print("Invalid input. Please enter a valid integer.")

    if not won :
        print("You failed to guess the number, Better luck next timr")
        print("The number was {secret_number}")
play_game()