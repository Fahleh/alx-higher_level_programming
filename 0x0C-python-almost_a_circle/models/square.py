#!/usr/bin/python3
"""Module that contains a class Square that
    inherits Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a class Square based on the class Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes an instance of Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Special str method"""
        str_square = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return str_square + str_id + str_xy + str_wh

    @property
    def size(self):
        """Get the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        self.width = value
        self.height = value

    def __str__(self):
        """Special str method """
        str_rectangle = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_size = "{}".format(self.size)

        return str_rectangle + str_id + str_xy + str_size

    def update(self, *args, **kwargs):
        """Update method """
        if args is not None and len(args) is not 0:
            attr_list = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if attr_list[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, attr_list[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns a dictionary with attributes"""
        attr_list = ['id', 'size', 'x', 'y']
        result = {}

        for key in attr_list:
            if key == 'size':
                result[key] = getattr(self, 'width')
            else:
                result[key] = getattr(self, key)

        return result
