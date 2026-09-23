"""Let the user input a number. Check if the number is

even or odd
is divisible by 5
is divisble by 5 and odd
"""

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
elif number % 2 == 1:
    print("Odd")

if number % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")
if number % 2 == 1 and number % 5 == 0:
    print("Divisible by 5 and is odd")