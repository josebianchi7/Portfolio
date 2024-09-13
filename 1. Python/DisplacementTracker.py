# Author: Jose Bianchi
# GitHub username: josebianchi7
# Description: Class object named Taxicab that describes a point on an x-y plane and tracks total movement

class Taxicab:
    """
    Represents the current position of a vehicle and tracks distance traveled based on input.
    Initializes an initial point for travel on an x-y plane and an odometer reading (displacement) of 0.
    """

    def __init__(self, x_coord, y_coord):
        """Creates private data members for class object."""
        self._x_coord = int(x_coord)
        self._y_coord = int(y_coord)
        self._odometer = 0

    def get_x_coord(self):
        """Returns current position for left/ right movement"""
        return self._x_coord

    def get_y_coord(self):
        """Returns current position for up/ down movement"""
        return self._y_coord

    def get_odometer(self):
        """Returns total distance traveled"""
        return self._odometer

    def move_x(self, x_shift):
        """based on left and right movement, returns new x_coord position and records movement to odometer"""
        self._x_coord += x_shift
        self._odometer += abs(x_shift)
        return self._x_coord

    def move_y(self, y_shift):
        """based on up and down movement, returns new y_coord position and records movement to odometer"""
        self._y_coord += y_shift
        self._odometer += abs(y_shift)
        return self._y_coord


if __name__ == '__main__':

    car = Taxicab(5, -8)
    car.move_x(3)
    car.move_y(-4)
    car.move_x(-1)
    print(car.get_x_coord())
    print(car.get_y_coord())
    print(car.get_odometer())
