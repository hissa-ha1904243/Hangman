import random
import hangman_words
import hangman_art

stages = hangman_art.stages
logo = hangman_art.logo
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
print(chosen_word)
print(hangman_art.logo)
guessIt = []
for l in chosen_word:
    guessIt.append("_")
print(guessIt)
lives = 6
end_of_game = False
while not end_of_game:
    guess = input("Guss a letter:").lower()
    for position in range(0, len(chosen_word)):
        letter = chosen_word[position].lower()
        if guess == letter:
            guessIt[position] = letter
    print(guessIt)
    if "_" not in guessIt:
        end_of_game = True
        print("You won!")
    if guess not in chosen_word:
        lives = lives - 1
        if lives == 0:
            end_of_game = True
            print("You Lost :(")
    print(stages[lives])