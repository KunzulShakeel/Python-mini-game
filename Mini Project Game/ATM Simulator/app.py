print('BANK AL-HABIB')
print("-----ATM-----")

amount = 20000
stored_pin = 1234

pin = int(input("Welcome please enter the pin:"))

while pin != stored_pin:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

while True:
    print("Select an option:")
    print("1. Deposit")
    print("2. Withdrawal")
    print("3. Check Balance")
    print("4. Transfer")
    print("5. Change PIN")
    print("6. Exit")

    option = int(input())

    if option == 1:
        deposit = int(input("Enter the amount you want to deposit:"))
        amount +=deposit
        print(f"Deposit Successful. New balance: {amount}.")
        
    elif option == 2:
       withdrawal = int(input("Enter the amount you want to widthdrawal:"))
       print(f"Withdrawal Successful. New balance: {amount}.")
       if withdrawal > amount:
        print("❌ Your amount cannot be withdrawn. Please check the amount.")
       else:
        amount -= withdrawal
        print(f"✅ Withdrawal Successful. New balance: {amount}.")

    elif option == 3:
       print(f"Your current amount is: {amount}")

    elif option == 4:
        transfer_amount = int(input("Enter the amount to transfer: "))
        if transfer_amount > amount:
            print("❌ Not enough balance to transfer.")
        else:
            receiver = input("Enter receiver's account number: ")
            amount -= transfer_amount
            print(f"✅ Transfer of {transfer_amount} to account {receiver} successful.")
            print(f"Remaining balance: {amount}")

    elif option == 5:
        old_pin = int(input("Enter your old PIN: "))
        if old_pin == pin:
            new_pin = int(input("Enter new PIN: "))
            pin = new_pin
            print("✅ PIN changed successfully.")
        else:
            print("❌ Incorrect old PIN.")

    elif option == 6:
        print("👋 Thank you for using BANK AL-HABIB ATM. Goodbye!")
        break
