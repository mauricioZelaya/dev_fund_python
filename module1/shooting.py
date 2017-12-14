import math


class Position(object):

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def x(self):
        return self._x

    def y(self):
        return self._y

    def distance_to(self, other):
        delta_x = self.x() - other.x()
        delta_y = self.y() - other.y()
        return math.sqrt(delta_x ** 2 + delta_y ** 2)

    def __eq__(self, other):
        if (isinstance(other, Position)):
            return self.x() == other.x() and self.y() == other.y()
        else:
            return False

    def __str__(self):
        return "(" + str(self._x) + ", " + str(self._y) + ")"


class Velocity(object):

    def __init__(self, start, end):
        self.create_from_positions(start, end)

    def create_from_positions(self, start, end):
        self._magnitude = end.distance_to(start)
        delta_y = end.y() - start.y()
        delta_x = end.x() - start.x()
        self._angle = math.degrees(math.atan2(delta_y, delta_x))

    @staticmethod
    def create_from_values(magnitude, angle):
        velocity = Velocity(Position(), Position())
        velocity._magnitude = magnitude
        velocity._angle = angle
        return velocity

    def magnitude(self):
        return self._magnitude

    def angle(self):
        # angle = tan-1(y/x)
        return self._angle


class Projectile(object):
    def __init__(self, position):
        self._position = position

    def shoot(self, velocity):
        start_position = self._position
        time = math.sqrt(2 * start_position.y() / 9.8)

        x = start_position.x() + velocity.magnitude() * time

        self._position = Position(x, 0)

    def position(self):
        return self._position
