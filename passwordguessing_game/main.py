import random
easy_words=["apple","train","money","nepal"]
medium_words=["python","bottle","monkey","laptop"]
hard_words=["elephant","diamond","computer","mountain"]

print("Welcome to the password guessing game.")
print("choose a difficulty level: easy,medium and hard")
level=input("Enter difficulty level: ").lower()

if level=="easy":
    secret=random.choice(easy_words)
elif level=="medium":
    secret=random.choice(medium_words)
elif level=="hard":
    secret=random.choice(hard_words)
else:
    print("Invalid choice.defaulting to easy level")
    secret=random.choice(easy_words)

attempts=0
print("\n Guess the secret password")

while True:
    guess= input("Enter your guesss: ").lower()
    attempts+=1

    if guess==secret:
        print(f"congratulations! you guessed in {attempts} attempts")
        break

    hint="" #empty string

    for i in range(len(secret)):
        if i <len(guess) and guess[i] == secret[i]:
            hint+=guess[i]
        else:
            hint+= "_"
    print("Hint:",hint)
print("GAME OVER")
