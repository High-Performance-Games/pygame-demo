import math

from pygame import Vector2

from object import Object
sunMass = 1.9885 * 10 ** 30
earthMass = 5.97219 * 10 ** 24
moonMass = 7.34767309 * 10 ** 22
objectMass = 1.0
sunRadius = 6.957 * 10 ** 8
earthRadius = 6.374 * 10 ** 6
moonRadius = 1.7374 * 10 ** 6
objectRadius = 100000
TotalRadius = earthRadius + objectRadius
TotalRadiusAskew = TotalRadius * TotalRadius
otherMass = 1.0
gravitationalConstant = 6.6743 * 10 ** -11
physicsScale = 10 ** 4


# gravitationalConstant = 6.6743 * 10 ** -1


def gravityForce(m1: float, m2: float, radius: float) -> float:
    g = ((m1 * m2) * gravitationalConstant) / (radius * radius)
    return g


def acceleration(F: float, m: float):
    return F / m


def gravityForce(o1: Object, o2: Object) -> float:
    radius = o1.position.distance_to(o2.position) * physicsScale
    g = ((o1.mass * o2.mass) * 6.6743 * 10 ** -11) / (radius * radius)
    return g


def gravityAcceleration(o1: Object, o2: Object) -> tuple[Vector2, Vector2]:
    Fg = gravityForce(o1, o2)
    displacement = (o2.position - o1.position).normalize()

    a1 = displacement * (Fg / o1.mass)
    a2 = -displacement * (Fg / o2.mass)
    return a1, a2


