"""
The maximum allowed luggage size for boarding an airplane is:

weight: 8kg
dimensions: 55x40x23cm (length x width x height)
Let the user input weight, length, width and height of the luggage. The program should check if the luggage
is allowed or not.
"""
max_weight = 8
max_dimensions = [55, 40, 23]

luggage_weight = int(input("Enter luggage weight (KG): "))
luggage_dimensions = ["length", "width", "height"]

if luggage_weight <= 8:
    for i in range(len(luggage_dimensions)):
        luggage_dimensions[i] = int(input(f"Enter luggage {luggage_dimensions[i]}: "))

        if luggage_dimensions[i] > max_dimensions[i]:
            print("Luggage is too large.")
            break
else:
    print("Luggage is too heavy.")