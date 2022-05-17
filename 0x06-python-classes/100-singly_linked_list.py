#!/usr/bin/python3
""" 2 class to create single linked list"""


class Node:
    """the node class to handle each individual node"""
    def __init__(self, data, next_node=None):
        """
        init to set the data for the new node
        args: data = int to go into node
        next_node = points to next node
        """
        if isinstance(data, int):
            self.__data = data
        else:
            TypeError("data must be an integer")
        if type(next_node) == Node or next_node is None:
            self.__next_node = next_node
        else:
            TypeError("next_node must be a Node object")

    @property
    def data(self):
        """
        returns node data
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        """
        sets value __data for node
        """
        if isinstance(value, int):
            self.__data = value
        else:
            TypeError("data must be an integer")

    @property
    def next_node(self):
        """
        returns node data
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """
        sets value __next_node for node
        """
        if type(value) == Node or value is None:
            self.__next_node = value
        else:
            TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """
    the node class to handle the whole list
    Nodes is the number of nodes in list
    """
    Nodes = 0

    def __init__(self):
        """
        init node to new head of None
        """
        self.__head = None

    def __str__(self):
        """
        Handles returning all the values in a string
        so it can be printed using the  print
        function
        """
        tmp = self.__head
        string = ""
        while tmp is not None:
            string += str(tmp.data)
            tmp = tmp.next_node
            if tmp is not None:
                string += '\n'
        return string

    def sorted_insert(self, value):
        """
        handles the insert of new nodes, and ensures they are in
        the correct order
        """
        if SinglyLinkedList.Nodes == 0:
            self.__head = Node(value)
            SinglyLinkedList.Nodes += 1
            return

        tmp = self.__head
        new_node = Node(value)
        if tmp.data >= value:
            new_node.next_node = tmp
            self.__head = new_node
            SinglyLinkedList.Nodes += 1
            return

        while tmp.next_node is not None:
            if (tmp.next_node.data >= value):
                break
            tmp = tmp.next_node
        new_node.next_node = tmp.next_node
        tmp.next_node = new_node
        SinglyLinkedList.Nodes += 1
