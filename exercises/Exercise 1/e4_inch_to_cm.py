while True:
    try:
        inches = float(input("Enter a value in inches: "))
        print(f"{inches} inches is {inches * 2.54} in centimeters.")
        break
    except ValueError:
        print("Input must be a number.")