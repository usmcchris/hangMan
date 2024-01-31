import random

def choose_word():
    words = ["xerox", "pneumonia", "semper fidelis", "xylophone", "python", "subliminal", "jinx", "wednesday", "hangman"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    print("Welcome to if You Don't Win, you're the Hangman!")
    secret_word = choose_word().lower()
    guessed_letters = []
    attempts = 6

    while True:
        current_display = display_word(secret_word, guessed_letters)
        print("\nCurrent word:", current_display)
        print("Guessed letters:", guessed_letters)

        if "_" not in current_display:
            print("\nYou got lucky! Let's see you do it again:", secret_word)
            break

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            attempts -= 1
            print("Incorrect guess! Attempts left:", attempts)
            if attempts == 0:
                print("Sorry, you ran out of attempts. The word was:", secret_word)
                break

if __name__ == "__main__":
    hangman()
