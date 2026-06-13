"""Pylint code example."""
#************* Module test
# pylint: disable=too-few-public-methods


class Car:
    """Represents a car."""

    def __init__(self, color):
        """Initialize a car with a color."""
        self.color = color


my_car = Car("Red")


def crash(car1, car2):
    """Simulate a crash between two cars."""
    car1.color = "Blue"
    car2.color = "Blue"


crash(Car("Red"), my_car)
