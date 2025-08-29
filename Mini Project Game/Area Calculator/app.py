print("Welcome to the area calculator 📐")
print("Choose a shape:")
print("1) Rectangle")
print("2) Triangle")
print("3) Square")
print("4) Circle")

choice = int(input("Enter your choice 1 - 3: "))

if choice == 1:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"The area of the rectangle is {area} square units.")
elif choice == 2:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is {area} square units.")
elif choice == 3:
    side = float(input("Enter the side of the square: "))
    area = side ** 2
    print(f"The area of the square is {area} square units.")
elif choice == 4:
    radius = float(input("Enter the radius of the circle: "))
    area = 3.14 * radius ** 2
    print(f"The area of the circle is {area} ")
else:
    print("Invalid choice. Please choose a number between 1 and 3.")
