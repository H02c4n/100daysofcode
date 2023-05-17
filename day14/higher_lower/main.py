from logo import logo, vs
from data import data
import random

def format_data(account):
    """Format the account data into printable format"""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_desc}, from {account_country}")

def check_answer(guess,a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

#Display logo
print(logo)
score = 0
game_should_continue = True

#Make the game repetable
while game_should_continue:

    #Generate a random account from the game data
    account_a = random.choice(data)
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
    #Format the account data into printable format
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    #Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    #Check if user is correct

    #Get follower count of each account
    a_follower_account = account_a["follower_count"]
    b_follower_account = account_b["follower_count"]
    #Use if statement to check if user is correct
    is_correct = check_answer(guess, a_follower_account, b_follower_account)
    #Give user feedback on their guess
    if is_correct:
        score +=1
        print(f"You are right! Current score: {score}.")
    else:
        print(f"Sorry, that is wrong.  Final score: {score}.")



#Making account at position B become the next account at position A

#Clear the screen
