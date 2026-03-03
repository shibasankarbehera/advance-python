word = "python"
guesses = ""
attempts = 6

print("Welcome to Guess The Word Game!")

while attempts > 0:
    failed = 0
    
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1
    
    print()
    
    if failed == 0:
        print(" You Won!")
        break
    
    guess = input("Guess a letter: ")
    guesses += guess
    
    if guess not in word:
        attempts -= 1
        print("Wrong guess ")
        print("Attempts left:", attempts)

if attempts == 0:
    print(" You Lost! The word was:", word)