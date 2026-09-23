"""
The information in the following table is stated in a medicine package. Also it is stated that for children
weight is more important than age.

Let the user input age and weight, and then the program should give out a dose
"""

while True:
    try:
        age = int(input("Enter your age: "))
        weight = int(input("Enter your weight: "))
        break
    except ValueError:
        print("Enter a valid whole number.")

# Adult & adolescent over 40 kg
if weight > 40 and age > 12:
    print("Number of pills: 1-2")

# Children 26-40, 7-12 years kg
elif weight >= 26 <= 40 and age >= 7 <= 12:
    print("Number of pills: 1/2-1")
    
# Children 15-25kg, 3-7 years
elif weight >= 15 <= 25 and age >= 3 <= 7:
    print("Number of pills: 1/2")