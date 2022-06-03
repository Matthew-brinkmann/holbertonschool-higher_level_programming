#!/usr/bin/python3
"""
Module contains Class Base:
"""
import json
import csv


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

    @classmethod
    def create(cls, **dictionary):
        """creates an instance of a subclass from dictionary"""
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """will return a list of instances from a file"""
        filename = cls.__name__ + ".json"
        retList = []
        try:
            with open(filename, 'r') as f:
                retList = cls.from_json_string(f.read())
            for i, string in enumerate(retList):
                retList[i] = cls.create(**retList[i])
        except Exception:
            return ([])
        return (retList)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes the list of objects to a file"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csvfile:
            csvWriter = csv.writer(csvfile)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    csvWriter.writerow([obj.id, obj.width, obj.height,
                                         obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    csvWriter.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        retList = []
        try:
            with open(filename, 'r', encoding='utf-8') as csvfile:
                csvReader = csv.reader(csvfile)
                for args in csvReader:
                    if cls.__name__ == "Rectangle":
                        dictionary = {"id": int(args[0]),
                                      "width": int(args[1]),
                                      "height": int(args[2]),
                                      "x": int(args[3]),
                                      "y": int(args[4])}
                    elif cls.__name__ == "Square":
                        dictionary = {"id": int(args[0]),
                                      "size": int(args[1]),
                                      "x": int(args[2]),
                                      "y": int(args[3])}
                        obj = cls.create(**dictionary)
                        retList.append(obj)
        except Exception:
            return ([])
        return retList
