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

    def update(self, *args, **kwargs):
        """Updates all the instances variables
        Args:
            args (tuple): a list of tuple that will be used to assign
            values for the instance variable
            kwargs (mapping): key value pairs
        """
        approved_set = {'id', 'size', 'x', 'y'}
        attribute_order = ['id', 'size', 'x', 'y']

        updated_attrs = {
                         attrs_key: attrs_value
                         for (attrs_key, attrs_value) in kwargs.items()
                         if attrs_key in approved_set
                         }

        for key, value in updated_attrs.items():
            setattr(self, key, value)

        for indx, ag_r in enumerate(args):
            setattr(self, attribute_order[indx], ag_r)

    def to_dictionary(self):
        """returns all the instance attributes as dictionary"""
        new_dict = {}

        for attr, value in self.__dict__.items():
            new_dict[attr.replace('_Rectangle__', '')] = value

        if "size" not in new_dict.keys():
            new_dict["size"] = new_dict["width"]
            del new_dict["width"]
            del new_dict["height"]

        return new_dict

    def __str__(self):
        name = type(self).__name__
        # TODO: value differ task 13
        return f"[{name}] ({self.id}) {self.x}/{self.y} - {self.size}"
