#!/usr/bin/python3
"""defines a singly linked list"""

class Node:
    """defines a singly linked list node class"""
    def __init__(self, data=0, next_node=None):
        """initilizes the data and next_node variables"""
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = data
        if not (next_node == None or isinstance(next_node, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        """retrieve data"""
        return self.__data
    @data.setter
    def data(self, value):
        """sets the value of data"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value
    @property
    def next_node(self):
        """retrieves the next node"""
        return self.__next_node
    @next_node.setter
    def next_node(self, value):
        """sets the next node"""
        if value is None:
            self.__next_node = None
        elif isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")

class SinglyLinkedList:
    """defines a SinglyLinkedList"""

    def __init__(self):
        """initilizes the class"""
        self.__head = None
    def __str__(self):
        stringg = ""
        current = self.__head
        while current is not None:
            if current.next_node is None:
                stringg += str(current.data)
            else:
                stringg += str(current.data) + "\n"
            current = current.next_node
        return stringg
    def sorted_insert(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        new_node = Node(value)
        current = self.__head
        if self.__head is None:
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            while current is not None:
                if current.next_node is None:
                    current.next_node = new_node
                    break
                elif current.next_node.data < value:
                    current = current.next_node
                else:
                    new_node.next_node = current.next_node
                    current.next_node = new_node
                    break
