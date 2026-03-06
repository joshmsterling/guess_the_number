import random
play_again = "y"

def check_guess(secret_number): 
    '''Loop to guess input and check against secret number'''        
    try:
        guess = int(input("Guess the Secret Number: "))

        if guess == secret_number:
            print("Correct")
            return True, True
        elif guess < secret_number:
            print("Higher")
            return False, True
        else:
            print("Lower")
            return False, True   
    except ValueError:
        print("Please enter Valid Number")
        return False, False

while True:

    secret_number = random.randint(1,100) #Generate number between 1-100
    attempts = 10 #Number of attempts left
    print("You have %d Attempts left" %attempts)

    while attempts > 0:
        
        correct, valid = check_guess(secret_number)

        if correct == True:
            score = attempts*10
            print("Score = %d" %score)
            break

        if valid == True:
            attempts -= 1 
            print("You have %d Attempts left" %attempts)
    if attempts == 0:
        print("You have run out of attempts! Score = 0. \nThe number was %d" %secret_number)    

    play_again = input("Play Again? (y/n): ").lower()
    while play_again != "y" and play_again != "n":
        print("Please Enter y or n!")
        play_again = input("Play Again? (y/n): ").lower()

    if play_again == "n":
        print("Thanks for Playing!")
        break