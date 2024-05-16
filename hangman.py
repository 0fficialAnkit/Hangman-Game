import random
def choose_word():
    words = ["apple", "banana", "orange", "grape", "strawberry", "watermelon", "palm"]
    return random.choice(words)
def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display
def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6
    print("Welcome to Hangman!")
    print("Try to guess the fruit.")
    while True:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.append(guess)
        if guess not in word:
            attempts -= 1
            print("Incorrect guess! You have {} attempts left.".format(attempts))
            if attempts == 0:
                print("You're out of attempts! The word was '{}'.".format(word))
                break
        else:
            print("Correct guess!")

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word '{}'!".format(word))
            break

if __name__ == "__main__":
    hangman()