#!/usr/bin/python3
"""Base class for all the other classes"""
import json


class Base():
    """Simple entry point for a whole project almost a circle
    Args:
        __nb_objects (int): private class variable
    """
    __nb_objects = 0

    def __init__(self, id=None) -> None:
        """Initializes instances variables
        Args:
            id (none): will be used to later on to update the private
            class variable
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def param_validator(self, name: str, param_value) -> None:
        """Simple function that i am going to use to test whether the
        value passed meet the required permissions

        Args:
            name (str): name of the attribute being tested
            param_value (int): actual attribute value
        Raises:
            raised two possible exception if one of the condition fails
        """
        if not isinstance(param_value, int):
            raise TypeError(f"{name} must be an integer")
        if param_value <= 0:
            raise ValueError(f"{name} must be > 0")

    @staticmethod
    def to_json_string(list_dictionaries):
        """from a python object to a json string"""
        lst = []
        if list_dictionaries is None:
            return "[]"

        for dicts in list_dictionaries:
            lst.append(dicts)

        return json.dumps(lst)

    @classmethod
    def save_to_file(cls, list_objs):
        """make a file containing a json format
        Args:
            cls (class): classmethod
            list_objs (list): python list object to turn into a json format
        """
        filename = f"{cls.__name__}.json"

        with open(filename, "w", encoding="utf-8") as file_pointer:
            lst = []
            if list_objs is None:
                file_pointer.write(cls.to_json_string(lst))

            for obj in list_objs:
                if type(obj) is cls:
                    lst.append(obj.to_dictionary())

            json_to_write = cls.to_json_string(lst)
            file_pointer.write(json_to_write)

    @staticmethod
    def from_json_string(json_string):
        """from json to python object(list dictionaries)
        Args:
            json_string: a string representation in json format
        """
        if json_string is None:
            return []
        if json_string == "" or not isinstance(json_string, str):
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates a dummy class object that has all the instance attributes

        Args:
            cls (class): a class object
            **dictionaries (**kwargs): key word arguments
        Return:
            returns the dummy instance which was created on the fly
        """
        # create a new instance object
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
            dummy.update(**dictionary)
            return dummy
        if cls.__name__ == "Square":
            dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Loads from a json file and then creates the class
        instances from the attributes loaded from file
        Args
            cls (class): a class instance
        Return:
            returns a list of instances
        """
        file_name = f"{cls.__name__}.json"
        try:
            with open(file_name, "r", encoding="utf-8") as f_pointer:

                lst = f_pointer.read()

                py_lst = cls.from_json_string(lst)
                dummy = [cls.create(**dicts) for dicts in py_lst]

                return dummy
        except FileNotFoundError:
            return []