print("🧙 Welcome To Terminal Advanture")
print("🌍 You are in a land full of mystery and magic....")
print("🗡️ Your goal is to find the legendary **Golden Sword of light**!")
print("🌲 You stand at the entrance of a dark, enchanted forest.")
print("🌄 There are two paths ahead:")
print("1️⃣ A dark, twisted path filled with shadows...")
print("2️⃣ A bright, glowing trail lit by magical light.")
print("✨ Which path do you choose?")

choice1 = input("Enter 1 or 2: ")

if choice1 == "1":
    print("🌑 You bravely step into the dark path...")
    print("👣 The trees whisper as you walk, and it gets darker with each step.")
    print("😨 You hear footsteps behind you. Something... or someone... is following you!")
    print("What do you want to do?")
    print("1️⃣ Keep going")
    print("2️⃣ Turn back")

    choice2 = input("Enter 1 or 2: ")

    if choice2 == "1":
        print("🏰 You run toward a mysterious light ahead...")
        print("✨ A glowing castle appears through the trees!")
        print("🪄 You enter and find a shimmering golden sword resting in the center of a stone table.")
        print("⚡ As you touch the sword, a surge of power flows through your veins...")
        print("🎉 Congratulations! You have found the **Golden Sword of Light** and completed your quest!")
    elif choice2 == "2":
        print("🧙‍♀️ You turn back... but it's too late!")
        print("💨 A dark witch appears from the shadows and casts a sleeping spell on you.")
        print("😴 You fall into an endless dream... Game Over.")
    else:
        print("❌ Invalid choice! You're lost forever in the dark forest... 🌲🌲🌲")

elif choice1 == "2":
    print("☀️ You walk into the glowing light path...")
    print("🌸 Birds chirp, flowers bloom, and the air feels magical.")
    print("🧚 A beautiful fairy appears, singing a soothing melody.")
    print("✨ She blesses you with luck and whispers:")
    print('"The sword you seek lies where shadows and light meet."')
    print("🧭 Your journey continues... To be continued!")
else:
    print("❌ Invalid choice! The forest closes in around you... You are lost.")
