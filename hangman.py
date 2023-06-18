import random

def hangman():
    word_list = ["apple", "banana", "cherry", "orange", "watermelon"]  
    word = random.choice(word_list)  
    guessed_letters = []  
    tries = 6  

    print("Welcome to Hangman!")
    print("_ " * len(word))  
    while tries > 0:
        guess = input("Guess a letter: ").lower()  

        
        if len(guess) != 1:
            print("Please enter a single letter.")
            continue
        elif not guess.isalpha():
            print("Please enter a letter.")
            continue
        elif guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)  

        if guess not in word:
            tries -= 1
            print("Wrong guess. Tries left:", tries)

        word_display = ""
        for letter in word:
            if letter in guessed_letters:
                word_display += letter + " "
            else:
                word_display += "_ "

        print(word_display)

        if "_" not in word_display:
            print("Congratulations! You guessed the word:", word)
            break

    if tries == 0:
        print("Game over! The word was:", word)

hangman()
