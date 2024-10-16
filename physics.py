import math

from object import Object

earthMass = 5.97219 * 10 ** 24
moonMass = 7.346 * 10 ** 22
earthRadius = 6.374 * 10 ** 6
moonRadius = 1737.4
TotalRadius = earthRadius + moonRadius
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
    radius = o1.position.distance_to(o2) * physicsScale
    g = ((o1.mass * o2.mass) * 6.6743 * 10 ** -11) / (radius * radius)
    return g


def gravityAcceleration(o1: Object, o2: Object) -> tuple[float, float]:
    radius = o1.position.distance_to(o2) * physicsScale
    Fg = gravityForce(o1.mass, o2.mass, radius)
    a1 = Fg / o1.mass
    a2 = Fg / o2.mass
    return a1, a2

    radius = o1.position.distance_to(o2) * physicsScale
    g = ((o1.mass * o2.mass) * 6.6743 * 10 ** -11) / (radius * radius)
    return g



