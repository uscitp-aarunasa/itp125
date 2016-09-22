def shut_down(s):
    if s == "yes":
        return "Shutting down"
    elif s =="no":
        return "Shutdown aborted"
    else:
        return "Sorry"

from math import sqrt
print sqrt(13689)


def distance_from_zero(dist):
    if type(dist) == int or type (dist) == float:
        return abs(dist)
    else:
        return "Nope"
