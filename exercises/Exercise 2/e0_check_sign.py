# Ask the user to input a number and check if this number is positive, negative or zero and print it out.
while True:
    try:
        number = int(input("Enter a whole number: "))

        if number > 0:
            print("Greater than 0.")
            break
        elif number == 0:
            print("Exactly 0.")
            break
        else:
            print("Less than 0.")
            break
    except ValueError:
        print("Input must be a whole number.")