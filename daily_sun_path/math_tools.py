import math

def sind(degree):
    return math.sin(math.radians(degree))


def cosd(degree):
    return math.cos(math.radians(degree))


def asind(degree):
    #arcsinus
    return math.degrees(math.asin(degree))


def range_mapping(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
