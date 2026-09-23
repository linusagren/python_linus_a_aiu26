# Ask the user to input a number and check if this number is positive, negative or zero and print it out.
while True:
    try:
        number = int(input("Enter a whole number: "))

        match number:
            case > 0:
                print("Number is bigger than 0!")
    except ValueError:
        print("Input must be a whole number.")