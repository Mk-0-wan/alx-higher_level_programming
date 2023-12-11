#!/usr/bin/python3
"""Square class that is inheriting from the parent class"""
from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle, Base):
    """Square that inherits from Class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Instance variable initializer

        Args:
            size (int): size of the square
            x (int): x value
            y (int): y value
            id (id): id of value to hold the class variable
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter function for the size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter function for the new value"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates all the instances variables
        Args:
            args (tuple): a list of tuple that will be used to assign
            values for the instance variable
            kwargs (mapping): key value pairs
        """
        # approved_set = {'id', 'size', 'x', 'y'}
        attribute_order = ['id', 'size', 'x', 'y']

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
                for k in ['x', 'size', 'y', 'id']
            }

        return new_dict

    def __str__(self):
        name = type(self).__name__
        return f"[{name}] ({self.id}) {self.x}/{self.y} - {self.size}"
