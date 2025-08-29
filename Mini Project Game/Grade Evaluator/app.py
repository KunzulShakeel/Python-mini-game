print("RESULT ANNOUNCMENT")

name = input("Enter your name: ")
standard = input("Enter your class: ")
marks = int(input("Enter your marks to know your grade: "))

if marks >= 90:
    print(f"Hello {name} of class {standard}, you're Grade is A+. \n🏆 Your dedication is inspiring — keep aiming higher!")

elif marks >= 80:
    print(f"Hello {name} of class {standard}, you're Grade is A. \n🌱 Growth in progress — your potential is unlimited!")

elif marks >= 70:
    print(f"Hello {name} of class {standard}, you're Grade is B. \n🔥 Solid performance! Stay focused and keep climbing.")

elif marks >= 60:
    print(f"Hello {name} of class {standard}, you're Grade is C. \n📈 Improvement starts with effort — and you're already on the path.")

elif marks >= 50:
    print(f"Hello {name} of class {standard}, you're Grade is D. \n💡 Failure is not the opposite of success — it's part of it")

else:
    print(f"\nHello {name} of class {standard}, your grade is F.\nIt’s okay to fall — what matters is getting back up. 💪")
