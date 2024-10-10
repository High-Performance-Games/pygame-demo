import math

from object import Object
earthMass = 5.97219 * 10 ** 24
gravitationalConstant = 6.6743 * 10 ** -11
def gravity(o1: Object, o2: Object) -> float:
    radius = 10
    g = ((o1.m * o2.m) * 6.6743 * 10 ** -11) / (radius * radius)
    return g
