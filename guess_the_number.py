import random
import json

def check_guess(secret_number): 
        '''Loop to guess input and check against secret number'''        
        try:
            guess = int(input("Guess the Secret Number: "))

            if guess == secret_number:
                print("Correct!")
                return True, True
            elif guess < secret_number:
                print("The Secret Number is Higher")
                return False, True
            else:
                print("The Secret Number is Lower")
                return False, True   
        except ValueError:
            print("Please enter Valid Number")
            return False, False
        
def display_leaderboard(leaderboard):
    '''Displays the current leaderboard ordered by descending total points'''
    print("\nLEADERBOARD\n")

    for player in sorted(leaderboard, key=lambda player_sort: leaderboard[player_sort]["total_score"], reverse=True):

        print("%s: \n Total Score: %d | Fewest Guesses: %s | Games Played: %d\n" %
            (player,
            leaderboard[player]["total_score"],
            leaderboard[player]["fewest_guesses"],
            leaderboard[player]["games_played"]))

def load_leaderboard():
    '''Searches for leaderboard file - loads if found - if not leaderboard is blank'''
    try:
        with open("leaderboard.json", "r") as leaderboard_file:
            return json.load(leaderboard_file)
    except FileNotFoundError:
        return {}

def save_leaderboard(leaderboard):
    '''Saves the leaderboard to .json to be opened next time the script runs'''
    with open ("leaderboard.json", "w") as leaderboard_file:
        json.dump(leaderboard, leaderboard_file, indent=2)

leaderboard = load_leaderboard()
       
while True:
    player_name = input("Enter Name: ")

    if player_name not in leaderboard:
        leaderboard[player_name] = {
        "total_score": 0,
        "games_played": 0,
        "fewest_guesses": None
    }
        print("Welcome New Player - %s" %player_name)
    else:
        print("Welcome back, %s" %player_name)

    while True:

        secret_number = random.randint(1,100) #Generate number between 1-100
        attempts = 10 #Number of attempts left
        print("\nYou have %d Attempts left" %attempts)

        won = False

        while attempts > 0:
            
            correct, valid = check_guess(secret_number)

            if correct == True:
                won = True
                score = attempts*10
                print("Score = %d" %score)
                break

            if valid == True:
                attempts -= 1 
                print("\nYou have %d Attempts left" %attempts)
        if attempts == 0:
            score = 0
            print("You have run out of attempts! Score = 0. \nThe number was %d" %secret_number)    
        
        guesses_used = 11 - attempts

        leaderboard[player_name]["games_played"] += 1
        leaderboard[player_name]["total_score"] += score
        if won == True:
            if leaderboard[player_name]["fewest_guesses"] is None or guesses_used < leaderboard[player_name]["fewest_guesses"]:
                leaderboard[player_name]["fewest_guesses"] = guesses_used

        save_leaderboard(leaderboard)
        display_leaderboard(leaderboard)


        play_again = input("Play Again? (y/n): ").lower()
        while play_again != "y" and play_again != "n":
            print("Please Enter y or n!")
            play_again = input("Play Again? (y/n): ").lower()

        if play_again == "n":
            print("Thanks for Playing %s!" %player_name)
            break
        
    new_player = input("New Player? (y/n): ").lower()
        
    while new_player != "y" and new_player != "n":
        print("Please Enter y or n!")
        new_player = input("New Player? (y/n): ").lower()

    if new_player == "n":
        print("Thanks for Playing!")
        break