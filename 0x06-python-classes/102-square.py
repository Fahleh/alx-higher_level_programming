#!/usr/bin/python3
"""Define a class - Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize the square.
        Args:
            size (int): Size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Define the operator == to the Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the operator != to the Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the operator < to the Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the operator <= to the Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the operator > to the Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the operator >= to the Square."""
        return self.area() >= other.area()
