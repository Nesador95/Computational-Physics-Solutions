# Done

import math as math

def from_cartesian_to_polar(x, y):
    x = float(x)
    y = float(y)

    r = math.sqrt(x**2 + y**2)
    theta = math.degrees(math.atan(y/x))

    return r, theta

print(from_cartesian_to_polar(input("input x: "), input("input y: ")))

    
