# import all the necessary files form external sources
import random
import hangman_words
import hangman_art

#list of word for hangman
#stetting of ascii figures and lives
word_list = hangman_words.word_list
stages = hangman_art.stages
lives = 6

# printing the ascii logo
logo_hangman = hangman_art.logo
print(logo_hangman)

# choosing random word
chosen_word = random.choice(word_list)

# making of the _ logic
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []


# loop that runs the game untill user doesn't win or lose
while not game_over:

    # lives information and game start
    print(f"****************************<???>/{lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print("You already guessed this letter: " + guess)

    display = ""
    if guess not in chosen_word:
        print(f"This letter: {guess} is not in the word, you lose a life!")
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)


    if guess not in chosen_word:
        lives -= 1

        if lives == 0:
            game_over = True

            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
