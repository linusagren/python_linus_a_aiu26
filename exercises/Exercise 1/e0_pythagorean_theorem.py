# a^2 + b^2 = c^2

import math

# A
a1 = 3**2
b1 = 4**2
c1 = math.sqrt(a1 + b1)

print(f"The hypothenuse is: {c1}.")

# B (B^2 = c^2 - a^2)

a2 = 5.0**2
c2 = 7.0**2
b2 = math.sqrt(c2 - a2)

print(f"The cathetus B is: {round(b2, 2)}")