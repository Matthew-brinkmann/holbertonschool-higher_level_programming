#!/usr/bin/python3
"""
Module contains Class Base:
"""
import json


class Base:
    """
    parent class to square and rectangle to handle
    the id attribute of all child classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init for Base Class"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns a json string of a dictionary"""
        if list_dictionaries is None:
            list_dictionaries = []
        return (json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """turns jason string into a dictionary"""
        if json_string is None or len(json_string) == 0:
            return ([])
        return (json.loads(json_string))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string of list_objs to a file"""
        filename = cls.__name__ + ".json"
        info = []
        if list_objs is not None:
            for i in list_objs:
                info.append(cls.to_dictionary(i))
        with open(filename, 'w', encoding="UTF-8") as f:
            f.write(cls.to_json_string(info))
