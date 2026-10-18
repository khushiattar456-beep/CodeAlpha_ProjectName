
import random

# List of words
words = ["python", "computer", "coding", "robot", "program"]

# Choose a random word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of wrong guesses allowed
wrong_guesses = 0
max_wrong_guesses = 6

print("=" * 40)
print("🎮 WELCOME TO HANGMAN!")
print("=" * 40)
print("Guess the word one letter at a time.")
print("You have 6 wrong guesses.\n")

# Create the hidden word
display_word = ["_"] * len(secret_word)

while wrong_guesses < max_wrong_guesses and "_" in display_word:

    print("Word:", " ".join(display_word))
    print("Guessed letters:", guessed_letters)
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    guess = input("Enter a letter: ").lower()

    # Check if input is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only one letter.\n")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter!\n")
        continue

    # Add the letter to guessed letters
    guessed_letters.append(guess)

    # Check whether the letter is in the word
    if guess in secret_word:

        print("✅ Good guess!")

        # Reveal the correct letter
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess

    else:
        wrong_guesses += 1
        print("❌ Wrong guess!")

    print()

# Game result
if "_" not in display_word:
    print("=" * 40)
    print("🎉 YOU WON!")
    print("The word was:", secret_word)
    print("=" * 40)

else:
    print("=" * 40)
    print("💀 GAME OVER!")
    print("The word was:", secret_word)
    print("=" * 40)
