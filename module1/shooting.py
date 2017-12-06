import math

class Position(object):

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def x(self):
        return self._x

    def y(self):
        return self._y

    def distance_to(self, position):
        delta_x = position.x()-self._x
        delta_y = position.y()-self._y
        if delta_x == 0 and delta_y == 0:
            return 0
        return math.sqrt((math.pow(delta_x, 2))+math.pow(delta_y, 2))


class Velocity(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def magnitude(self):
        return self.end.distance_to(self.start)

    def angle(self):
        delta_x = self.end.x() - self.start.x()
        delta_y = self.end.y() - self.start.y()
        return math.degrees(math.atan(delta_y/delta_x))


