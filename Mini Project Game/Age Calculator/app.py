print("-----Welcome-----")
print("🎩 We'll guess your age!")

num = int(input("🧙🏻‍♂️ Enter a number between 1 - 9: "))

step1 = (num * 2 + 5) * 50

current_year = int(input("🧙🏻‍♂️ Enter the current year : "))

birthday_passed = input("🧙🏻‍♂️🔮 your birthday has already passed (yes/no): ")
print("🧙🏻‍♂️Trust the process!")

if birthday_passed == "yes":
    step2 = step1 + current_year

else:
    step2 = step1 + current_year - 1

birth_year = int(input("🪄 Enter your birth year: "))
print("🎉 We're almost there!")

final_result = step2 - birth_year - 250

print("🎊 Your age is: ", final_result)
print("🧠 The first digit is the number you chose.")
print("🎂 The last two digits are your age (if birthday info is correct).")
