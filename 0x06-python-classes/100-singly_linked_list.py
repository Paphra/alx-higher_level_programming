#!/usr/bin/python3
"""100-singly_linked_list module
For a sjngly list node class
"""


class Node:
    """Class Node
    defines a node of a singly linked list
    Args: None
    Atteibutes:
        __data (int): an kntwger for node data
        __next_node (Node): a Node or None
    """

    def __init__(self, data, next_node=None):
        """__init__ method
        Initializes the private and public attributes
        Args:
            data (int): and integer fof data of the Node
            next_node (Node): represents a Node next or None
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """get data value
        A property method for getting the data
        Rwturns: data value
        """

        return self.__data

    @data.setter
    def data(self, value):
        """set data value
        A setter method for setting the value of the data attribute
        Args:
            value (int): the value integer
        Todo:
            * check for data type, int, else TypeError
        Returns: None
        """

        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """get next node element
        A property to get the next node
        Returns: the next nkde or None
        """

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """set next_node
        A setter method for setting the next node element
        Args:
            value (Node): a node or None
        Todo:
            * check for data type, Node, or None, otherwise TypeError
        Return: None
        """

        if not isinstance(value, Node) and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """Class SinglyLinkedList
    A printable class that represents a Singly linked list
    Args: None
    Attributes:
        __head (Node): the startin element of the list
    """

    def __init__(self):
        """__init__ method
        Initializes the attributes
        """

        self.__head = None

    def __str__(self):
        """__str__ method
        Prints out the node list
        Returns: str
        """

        tmp = self.__head
        result = ""
        while tmp is not None:
            result += "{:d}".format(tmp.data)
            tmp = tmp.next_node
            if tmp is not None:
                result += "\n"
        return result

    def sorted_insert(self, value):
        """sorted_insert method
        inserts a new Node into the correct sorted position in the list
        Args:
            value (int): value for the data attribute
        Returns: None
        """

        new_node = Node(value, next_node=None)
        if self.__head is None:
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while tmp.next_node is not None and tmp.next_node.data < value:
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node
