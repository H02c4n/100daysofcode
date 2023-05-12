import random
from art import logo, stages
from wordlist import word_list
print(logo)


chosen_word = random.choice(word_list)
word_lenght = len(chosen_word)

end_of_game = False
lives = 6

display = []
for _ in range(word_lenght):
    display += "_"


while not end_of_game:

    guess = input("Guess a letter\n").lower()
    # Check guessed letter
    for position in range(word_lenght):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that is not in the word. You lose a life.")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose")
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win")
    print(stages[lives])