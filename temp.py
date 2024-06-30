

# Convert from Celsius to Fahrenheit
def celsius_To_Fahrenheit(celsius):
    return (celsius * 9.0/5.0) + 32


# function convert Fahrenheit to Celsius
def Fahrenheit_To_Celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0 / 9.0


# Function Celsius to Kelvin
def celsius_To_Kelvin(celsius):
    return celsius + 273.15


# Function to convert Kelvin to Celsius
def kelvin_To_Celsius(kelvin):
    return kelvin - 273.15


# Function Fahrenheit to Kelvin
def Fahrenheit_To_Kelvin(fahrenheit):
    return celsius_To_Kelvin(Fahrenheit_To_Celsius(fahrenheit))


# Function to convert kelvin to Fahrenheit
def kelvin_To_Fahrenheit(kelvin):
    return celsius_To_Fahrenheit(kelvin_To_Celsius(kelvin))


# Menu function - display menu and get user's choice
def menu():
    print("Welcome to Temperature Menu")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print('3. Celsius to Kelvin')
    print('4. Kelvin to Celsius')
    print('5. Fahrenheit to Kelvin')
    print('6. Kelvin to Fahrenheit')
    print('0. Exit')
    userChoice = -1

    while userChoice < 0 or userChoice > 6:
        userChoice = int(input("Enter choice: "))

        if userChoice < 0 or userChoice > 6:
            print("Invlaid input - enter 0-6")

    return userChoice


if __name__ == "__main__":

    choice = menu()

    while choice != 0:

        # Read input
        value =float(input("Enter temperature to convert: "))
        

        if choice == 1:
            # c to f
            print(f"{value:.2f} Celsius to Fahrenheit {Celsius_to_Fahrenheit(value):.2f}")
        elif choice == 2:
            # f to c
            print(f"{value:.2f} Fahrenheit to Celsius {Fahrenheit_to_Celsius(value):.2f}")
        elif choice == 3:
            # c to k
            print(f"{value:.2f} Celsius to Kelvin {Celsius_to_Kelvin(value):.2f}")
        elif choice == 4:
            # k to c
            print(f"{value:.2f} Kelvin to Celsius {Kelvin_to_Celsius(value):.2f}")
        elif choice == 5:
            # f to k
            print(f"{value:.2f} Fahrenheit to Kelvin {Fahrenheit_to_Kelvin(value):.2f}")
        elif choice == 6:
            # k to f
            print(f"{value:.2f} Kelvin to Fahrenheit {Kelvin_to_Fahrenheit(value):.2f}")
        else:
            print("invalid!")

        print()

        choice = menu()