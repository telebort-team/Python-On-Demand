ans = 34
guess = None

while guess != ans:
    guess = int(input("Guess the number: "))
    if guess > ans:
        print("The guess is too big")
    elif guess < ans:
        print("The guess is too small")
    else:
        print("Congratulation! You guessed the correct number!")
