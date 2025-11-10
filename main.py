"""
    Pharmacy Chatbot Program with Doctor PIN Login + Age Restriction + Doctor Prescription View
"""

def get_user_name():
    return input("Please enter your name: ")

def greet_user(name):
    print(f"Hello, {name}!")

def get_age():
    return int(input("Please enter your age: "))

# Store prescriptions
prescriptions = {}

# Doctor PIN
DOCTOR_PIN = "1234"

def doctor_menu():
    while True:
        print("\n--- Doctor Menu ---")
        print("1. Add a prescription")
        print("2. View all prescriptions")
        print("3. Return to main menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            patient = input("Enter patient name: ")
            prescription_name = input("Enter prescription name: ")
            refills = int(input("Enter number of refills allowed: "))

            prescriptions[prescription_name] = refills
            print(f"Prescription '{prescription_name}' for {patient} added with {refills} refills.")

        elif choice == "2":
            if prescriptions:
                print("\n--- Prescription List ---")
                for name, refills in prescriptions.items():
                    print(f"{name} - Refills left: {refills}")
            else:
                print("No prescriptions in the system yet.")

        elif choice == "3":
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Try again.")

def main():
    user_name = get_user_name()
    greet_user(user_name)
    age = get_age()
    print(f"Oh, you are {age}!")

    while True:
        print("\n Please choose from the menu for the pharmacy:")
        print("1. Are you a medical practitioner?")
        print("2. Are you checking status of prescription?")
        print("3. Are you looking for refill prescription?")
        print("4. Exit")
        choice = input("Enter your choice: ")

        # Doctor Access
        if choice == "1":
            entered_pin = input("Enter doctor PIN: ")
            if entered_pin == DOCTOR_PIN:
                print("PIN correct. Access granted.")
                doctor_menu()
            else:
                print("Incorrect PIN. Access denied.")

        # Check prescription
        elif choice == "2":
            prescription_name = input("Enter the name of the prescription: ")
            if prescription_name in prescriptions:
                print(f"Prescription found! Refills remaining: {prescriptions[prescription_name]}")
            else:
                print("This prescription is not in our system.")

        # Refill prescription (Age Restriction)
        elif choice == "3":
            if age < 18:
                print("You are under 18. You must be 18+ to refill prescriptions without a guardian or doctor.")
                continue

            prescription_name = input("Enter the prescription to refill: ")
            if prescription_name in prescriptions:
                if prescriptions[prescription_name] > 0:
                    prescriptions[prescription_name] -= 1
                    print(f"Prescription refilled! Remaining refills: {prescriptions[prescription_name]}")
                else:
                    print("No refills remaining. Contact your doctor.")
            else:
                print("This prescription is not in our system.")

        elif choice == "4":
            print("Have a nice rest of the day!")
            break

        else:
            print("Can you enter the option as in the menu?")

if __name__ == "__main__":
    main()
