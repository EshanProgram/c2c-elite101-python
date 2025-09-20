
"""
    Welcome to Elite 101 this program is a starter for your chatbot project.
    The starter prompts the user to enter their name and then greets them with a personalized message.

    Functions:
        get_user_name(): Prompts the user to enter their name and returns it.
        greet_user(name): Prints a greeting message using the provided name.
        main(): Main function that orchestrates the user input and greeting process.

    Execution:
        When the script is run directly (not imported as a module), it will execute the main() function.
"""


def get_user_name():
    return input("Please enter your name: ")

def greet_user(name):
    print(f"Hello, {name}!")

def get_age():
    return input("Please enter your age: ")

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
        choice = input("Enter your choice:")
        
        if choice == "1":
            print("Go to sub menu 1 (placeholder)")
        elif choice == "2":  
            print("Go to sub menu 2 (placeholder)")
        elif choice == "3":  
            print("Go to sub menu 3 (placeholder)")   
        elif choice == "4":  
            print("Have a nice rest of the day")
            break
        else:
            print("Can you enter the option as in the menu")

if __name__ == "__main__":
    main()
