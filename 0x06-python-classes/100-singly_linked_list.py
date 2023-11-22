"""Singly Linked list in python"""


class Node:
    """Node class that is used to make a linkedlist

    Attributes:
        data (int): used to store the data of the node
        next_node (unknown): used to hold the value of the next node

    """
    def __init__(self, data, next_node=None):
        """Initializes the value of the instances variables for class Node

        Args:
            data (int): Param to hold the value of the new node data
            next_node (unknown): Param to hold the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Just returns the data instance value

        Return:
            returns the instances variables for the class Node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Sets a new value to the private instance variable value, it mutates the private value

        Args:
            value (int): the new value for the private size
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrives the next node value

        Return:
            returns the next node value
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node with a new value

        Args:
            value (Node): just a new node that is to be created
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""New node generator"""


class SinglyLinkedList:
    """A new class for SinglyLinkedList creation"""
    def __init__(self):
        """initialize the SinglyLinkedList instance variables"""
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new node into the corrected node position"""
        curr = self.__head

        if (curr is None):
            n_node = Node(value, self.__head)
            self.__head = n_node
            return

        if (curr.data > value):
            self.__head = Node(value)
            self.__head.next_node = curr
        else:
            while curr.next_node is not None:
                if curr.next_node.data > value:
                    break
                curr = curr.next_node
            n_node = Node(value, curr.next_node)
            curr.next_node = n_node
            return

    def __str__(self):
        """Prints the string values"""
        data = []
        curr = self.__head
        while curr is not None:
            data.append(str(curr.data))
            curr = curr.next_node
        return "\n".join(data)
