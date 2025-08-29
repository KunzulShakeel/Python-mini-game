import random

print("Welcome to Magic 8 Ball🎱")
print("Ask a question, and I'll respond with a mysterious answer.")

Question = input("Ask me any yes/no question... if you dare 👀:")

play_again = "yes"

while play_again == "yes":
    question = input("What is your question?")

    if question.strip() == "":
        print("Please enter a question")
    else:
        answer = random.choice([
            "Yes, definitely. 🌟",
            "No way. ❌",
            "Hmm... maybe. 🤔",
            "Ask again later. 💤",
            "I’m not sure... try again. 🌀",
            "Looks good! ✅",
            "Outlook not so good... ⚠️"
        ])
        print("Magic Ball 🎱 says:",answer)
    play_again = input("Do you want to ask another question? (yes/no): ").lower()
print("Thanks for playing! 👋")
