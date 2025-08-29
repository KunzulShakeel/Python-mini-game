import random

print("-----Welcome-----")
print("🎯 Let's play 'Guess the Number'!")
print("I'm thinking of a number between 1 and 100.")
print("You have 6 chances to guess it correctly.")
print("If you're wrong, I'll give a hint. Let's begin!")


number = random.randint(1, 100)

tries = 6
guesses = 0

while guesses < tries:
    guess = int(input("🔢 Guess a number: "))
    guesses += 1

    if guess == number:
        print("🎉 You guessed it! You win!")
        break
    elif guess < number:
        print("📈 Too low! Try a higher number.")
    else:
        print("📉 Too high! Try a lower number.")

    print(f"💡 Tries left: {tries - guesses}")

if guesses == tries and guess != number:
    print(f"😢 Out of tries! The correct number was {number}.")
