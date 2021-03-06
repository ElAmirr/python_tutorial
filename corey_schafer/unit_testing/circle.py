from math import pi


def circle_area(r):
    if not(isinstance(r, int) or isinstance(r, float)):
        raise TypeError("The radius must be a non-negative real number.")

    if r < 0:
        raise ValueError("the radius cannot be negative")
    return pi*(r**2)


# test function
radii = [2, 0, -3, 2 + 5j, True, "radius"]
message = "Area of cirles with r = {radius} is{area}."

for r in radii:
    A = circle_area(r)
    print(message.format(radius=r, area=A))
