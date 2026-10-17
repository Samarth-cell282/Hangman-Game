import random

def play_hangman():
    # 1. Use a small list of 5 predefined words
    words = ["python", "code", "hangman", "program", "developer"]
    
    # Randomly select a word from the list
    secret_word = random.choice(words)
    
    # Track guessed letters and game state
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6  # Limit incorrect guesses to 6

    print("=== Welcome to Hangman! ===")

    # Game loop using a while loop
    while incorrect_guesses < max_incorrect_guesses:
        # Display the current state of the word (e.g., "p _ t h o n")
        word_display = ""
        for letter in secret_word:
            if letter in guessed_letters:
                word_display += letter + " "
            else:
                word_display += "_ "
        
        print("\nWord:", word_display.strip())
        print(f"Incorrect guesses remaining: {max_incorrect_guesses - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        
        # Check if player has guessed all letters (Win condition)
        if all(letter in guessed_letters for letter in secret_word):
            print("\n🎉 Congratulations! You guessed the word correctly!")
            break

        # Get player input
        guess = input("Guess a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        # Add the valid guess to our tracked letters
        guessed_letters.append(guess)

        # Check if the guess is in the secret word using if-else
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")

    # Check if the player ran out of attempts (Loss condition)
    if incorrect_guesses == max_incorrect_guesses:
        print("\n❌ Game Over! You ran out of guesses.")
        print(f"The secret word was: {secret_word}")

# Start the game
if __name__ == "__main__":
    play_hangman()