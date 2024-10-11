import math

from object import Object

earthMass = 5.97219 * 10 ** 24
# earthMass = 5.97219 * 10 ** 14
objectMass = 1.0
earthRadius = 6.374 * 10 ** 6
objectRadius = 0.1
TotalRadius = earthRadius + objectRadius
TotalRadiusAskew = TotalRadius * TotalRadius
otherMass = 1.0
gravitationalConstant = 6.6743 * 10 ** -11


# gravitationalConstant = 6.6743 * 10 ** -1


def gravityForce(m1: float, m2: float, radius: float) -> float:
    g = ((m1 * m2) * gravitationalConstant) / (radius * radius)
    return g


def acceleration(F: float, m: float):
    return F / m


def gravityObjects(o1: Object, o2: Object) -> float:
    radius = 10
    g = ((o1.m * o2.m) * 6.6743 * 10 ** -11) / (radius * radius)
    return g


Fg = gravityForce(earthMass, objectMass, TotalRadius)
g = acceleration(Fg, objectMass)
print("Force: ", Fg, "Gravity: ", g)
