#!/usr/bin/python3
"""Simple implementation of the Bubble sort algorithm"""


class BinarySearchTree():
    """Making a simple binary search tree"""

    def __init__(self, root):
        """Initialize the class with the a value"""
        self.left = None
        self.right = None
        self.root = root

    def insert_node(self, value):
        """Inserting new value to the BST"""
        # check if value is less than root value
        if self.root > value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert_node(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert_node(value)

    def in_order_traversal(self):
        """Printing the first left node then right node"""
        if self.left:
            self.left.in_order_traversal()
        print(self.root)
        if self.right:
            self.right.in_order_traversal()

    def get_the_rightmost_node(self):
        """Finding the rightmost node"""
        current = self
        while (current.right):
            current = current.right
        return current


def find_peak(list_of_integers):
    """"Finding the peak value using BST"""
    if len(list_of_integers) == 0:
        return None

    bst = BinarySearchTree(0)

    for i in list_of_integers:
        bst.insert_node(i)

    peak_val = bst.get_the_rightmost_node()

    return (peak_val.root)
