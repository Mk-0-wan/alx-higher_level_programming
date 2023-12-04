#!/usr/bin/python3
"""
A python rebel class that overwrites some methods
of the int class
Cool thing to note if methods share the same structure
you are able to mutate them with the super()
"""


class MyInt(type(3)):
    """MyInt is a class that renegade
    some of the int class function
    """

    def __ne__(self, other) -> bool:
        """A python builtin function which checks if two
        values are not equal. But returns unexpected result
        which is the same as __eq__().

        Args:
            other (object): another instance of the same
            class to perform the != operation
        Return:
            uses the super() builtin to change the use case
            of the != to == operation hence unexpected behavior
            is to be expected
        """
        super().__eq__(other)

    def __eq__(self, other) -> bool:
        """A python builtin function which checks if two
        values are equal. But returns unexpected result
        which is the same as __ne__()

        Args:
            other (object): another instance of the same
            class to perform the == operation
        Return:
            uses the super() builtin to change the use case
            of the == to != operation hence unexpected behavior
            is to be expected
        """
        super().__ne__(other)
