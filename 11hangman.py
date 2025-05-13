import random

word_list = ["apple", "snowfall", "kashmir"]
lives = 6
chosen_word = random.choice(word_list)

print(chosen_word)  # Step 1: Random word from the list

# Step 2: Display "_" for each letter
display = []
for i in range(len(chosen_word)):
    display += '_'
print(display)

game_over = False


while not game_over:
    guessed_letter = input("Guess the letter: ").lower()


    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter

    print(display)

    
    if guessed_letter not in chosen_word:
        lives -= 1
        print("Wrong guess! Lives left:")
        if lives == 0:
            game_over = True
            print("You lose!!:", chosen_word)

    
    if '_' not in display:
        game_over = True
        print("You win!!")





