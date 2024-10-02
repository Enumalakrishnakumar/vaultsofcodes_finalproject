import random

def get_random_word():
    """Return a random word from a predefined list."""
    words = ['python', 'hangman', 'programming', 'challenge', 'coding']
    return random.choice(words)

def display_word(word, guessed_letters):
    """Display the word with guessed letters and underscores for remaining letters."""
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = get_random_word()
    guessed_letters = set()
    incorrect_guesses = set()
    max_attempts = 10
    attempts_left = max_attempts

    print("Welcome to Hangman!")
    
    while attempts_left > 0:
        print("\n" + display_word(word, guessed_letters))
        print(f"Incorrect guesses: {' '.join(incorrect_guesses)}")
        print(f"Attempts left: {attempts_left}")
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters or guess in incorrect_guesses:
            print("You've already guessed that letter.")
            continue

        if guess in word:
            guessed_letters.add(guess)
            if set(word) <= guessed_letters:
                print(f"\nCongratulations! You've guessed the word: {word}")
                break
        else:
            incorrect_guesses.add(guess)
            attempts_left -= 1

    if attempts_left == 0:
        print(f"\nSorry, you've run out of attempts. The word was: {word}")

if __name__ == "__main__":
    hangman()