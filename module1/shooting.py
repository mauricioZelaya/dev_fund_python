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

    def __eq__(self, other):
        if isinstance(other, Position):
            return self.x() == other.x() and self.y() == other.y()
        else:
            return False

    def __str__(self):
        return "("+str(self.x())+", "+str(self.y())+")"


class Velocity(object):
    def __init__(self):
        self._magnitude = 0
        self._angle = 0
        self._start = Position()
        self._end = Position()

    def create_from_positions(self, start, end):
        self._magnitude = end.distance_to(start)
        delta_x = self._end.x() - self._start.x()
        delta_y = self._end.y() - self._start.y()
        self._angle = math.degrees(math.atan(delta_y/delta_x))

    def create_from_values(self, magnitude, angle):
        self._magnitude = magnitude
        self._angle = angle

    def magnitude(self):
        return self._magnitude

    def angle(self):
        return self._angle


class Projectile(object):
    def __init__(self, position):
        self._position = position

    def shoot(self, velocity):
        pass

    def position(self):
        return Position(5, 0)


