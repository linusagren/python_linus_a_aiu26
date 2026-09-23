"""
The maximum allowed luggage size for boarding an airplane is:

weight: 8kg
dimensions: 55x40x23cm (length x width x height)
Let the user input weight, length, width and height of the luggage. The program should check if the luggage
is allowed or not.
"""

luggage_weight = int(input("Enter luggage weight (KG): "))
luggage_dimensions = [0, 0, 0]

for i in range(len(luggage_dimensions)):
    match i:
        case 0:
            luggage_dimensions[i] = int(input("Enter luggage length: "))
        case 1:
            luggage_dimensions[i] = int(input("Enter luggage width: "))
        case 2:
            luggage_dimensions[i] = int(input("Enter luggage height: "))

