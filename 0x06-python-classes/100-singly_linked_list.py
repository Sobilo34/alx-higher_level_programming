#!/usr/bin/python3
"""Define a class Node for singly linked list."""


class Node:
    """Represent a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
            data (int): The data of the node.
            next_node (Node, optional): Next node in list. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get or set the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node.

        Args:
            value (int): The data of the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get or set the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node.

        Args:
            value (Node or None): The next node in the list.

        Raises:
            TypeError: If value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly linked list."""

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.head = None

    def sorted_insert(self, value):
        """Insert a new Node into correct sorted position in list (asc order).

        Args:
            value (int): The data of the new node.
        """
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            curr = self.head  # curr -> current
            while curr.next_node is not None and curr.next_node.data < value:
                curr = curr.next_node
            new_node.next_node = curr.next_node
            curr.next_node = new_node

    def __str__(self):
        """Print the entire list."""
        result = []
        curr = self.head
        while curr is not None:
            result.append(str(curr.data))
            curr = curr.next_node
        return '\n'.join(result)
