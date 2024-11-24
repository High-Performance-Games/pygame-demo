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
sunToEarth = 1.5 * 10 ** 11
sunToVenus = 1.0 * 10 ** 11
moonToEarth = 3.85 * 10 ** 8
earthVelocity = 29784.8
moonVelocity = 1022.8
gravitationalConstant = 6.6743 * 10 ** -11


# gravitationalConstant = 6.6743 * 10 ** -1


def acceleration(F: float, m: float):
    return F / m


def gravityForce(o1: Object, o2: Object) -> float:
    radius = o1.position.distance_to(o2.position)
    Fg = ((o1.mass * o2.mass) * 6.6743 * 10 ** -11) / (radius * radius)
    displacement = (o2.position - o1.position).normalize()
    o1.force += Fg * displacement
    o2.force += Fg * -displacement
    return Fg


def gravityAcceleration(o1: Object, o2: Object) -> tuple[Vector2, Vector2]:
    Fg = gravityForce(o1, o2)
    displacement = (o2.position - o1.position).normalize()

    a1 = displacement * (Fg / o1.mass)
    a2 = -displacement * (Fg / o2.mass)
    o1.acceleration += a1
    o2.acceleration += a2
    return a1, a2


