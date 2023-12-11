#!/usr/bin/python3
"""A rectangle class that inherits from Base class"""
from models.base import Base


class Rectangle(Base):
    """docstring for Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes all the instance attributes
        Args:
            width (int): an integer value holding the with of the Rectangle
            height (int): height of the rectangle
            x (int): just an x value
            y (int): just a y int value
            id (int): id value
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Simple width getter"""
        return self.__width

    @property
    def height(self):
        """Simple height getter"""
        return self.__height

    @property
    def x(self):
        """Simple x getter"""
        return self.__x

    @property
    def y(self):
        """Simple y getter"""
        return self.__y

    @width.setter
    def width(self, value):
        """Simple width setter
        Args:
            value (int): new value to assign to the instance attribute
        Return:
            returns a new mangled width for the instance variable
        """
        self.param_validator('width', value)
        self.__width = value

    @height.setter
    def height(self, value):
        """Simple width setter
        Args:
            value (int): new value to assign to the instance attribute
        Return:
            returns a new mangled width for the instance variable
        """
        self.param_validator('height', value)
        self.__height = value

    @x.setter
    def x(self, value):
        """Simple width setter
        Args:
            value (int): new value to assign to the instance attribute
        Return:
            returns a new mangled width for the instance variable
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Simple width setter
        Args:
            value (int): new value to assign to the instance attribute
        Return:
            returns a new mangled width for the instance variable
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of a Rectangle"""
        return self.__width * self.__height

    def display(self) -> None:
        """Prints the the result in an ascii form"""
        if self.width == 0 or self.height == 0:
            print("")
        x_val = self.x
        y_val = self.y
        # print(f'{x_val} * {y_val} = {x_val * y_val}')
        if y_val > 0:
            print("\n" * y_val, end='')
        for _ in range(self.height):
            print(" " * x_val + "#" * self.width)

    def __str__(self):
        """How to print out the file it the specified order"""
        cls_name = type(self).__name__
        return f"[{cls_name}] ({self.id}) {self.__x}/{self.__y} \
- {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Updates all the instances variables
        Args:
            args (tuple): a list of tuple that will be used to assign
            values for the instance variable
            kwargs (mapping): key value pairs
        """
        # avoid duplicate values
        attribute_order = ['id', 'width', 'height', 'x', 'y']

        for indx, ag_r in enumerate(args):
            if indx < len(attribute_order):
                setattr(self, attribute_order[indx], ag_r)

        if args:
            return

        for key, value in kwargs.items():
            if key in attribute_order:
                setattr(self, key, value)

    def to_dictionary(self):
        """returns all the instance attributes as dictionary"""
        new_dict = {
                k: getattr(self, k)
                for k in ['x', 'width', 'y', 'id', 'height']
                }
        return new_dict
