#!/usr/bin/python3
from tokenize import single_quoted


class Node:
    def __init__(self, data, next_node=None):
        if type(data) == int:
            self.__data = data
        else:
            TypeError("data must be an integer")
        if type(next_node) == Node or next_node is None:
            self.__next_node = next_node
        else:
            TypeError("next_node must be a Node object")

    @property
    def data(self):
        return (self.__data)

    @data.setter
    def data(self, value):
        if type(value) == int:
            self.__data = value
        else:
            TypeError("data must be an integer")

    @property
    def next_node(self):
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if type(value) == Node or value is None:
            self.__next_node = value
        else:
            TypeError("next_node must be a Node object")


class SinglyLinkedList:
    Nodes = 0

    def __init__(self):
        self.__head = None

    def __str__(self):
        tmp = self.__head
        string = ""
        while tmp is not None:
            string += str(tmp.data)
            tmp = tmp.next_node
            if tmp is not None:
                string += '\n'
        return string

    def sorted_insert(self, value):
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
