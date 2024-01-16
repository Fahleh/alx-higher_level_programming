#!/usr/bin/python3
"""Module for base class"""
import json
import csv
import os.path


class Base:
    """Base class for all classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation"""
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes object to a file """
        filename = "{}.json".format(cls.__name__)
        d_list = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                d_list.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(d_list)

        with open(filename, 'w') as fd:
            fd.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """Returns a dictionary from a JSON string"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with attributes set"""
        if cls.__name__ == "Rectangle":
            instance = cls(10, 10)
        else:
            instance = cls(10)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as fd:
            str_list = fd.read()

        cls_list = cls.from_json_string(str_list)
        ins_list = []

        for index in range(len(cls_list)):
            ins_list.append(cls.create(**cls_list[index]))

        return ins_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves a file as CSV"""
        filename = "{}.csv".format(cls.__name__)

        if cls.__name__ == "Rectangle":
            d_list = [0, 0, 0, 0, 0]
            keys_list = ['id', 'width', 'height', 'x', 'y']
        else:
            d_list = ['0', '0', '0', '0']
            keys_list = ['id', 'size', 'x', 'y']

        result = []

        if not list_objs:
            pass
        else:
            for obj in list_objs:
                for kv in range(len(keys_list)):
                    d_list[kv] = obj.to_dictionary()[keys_list[kv]]
                result.append(d_list[:])

        with open(filename, 'w') as fd:
            writer = csv.writer(fd)
            writer.writerows(result)

    @classmethod
    def load_from_file_csv(cls):
        """ Method that loads a CSV file """
        filename = "{}.csv".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as fd:
            reader = csv.reader(fd)
            csv_list = list(reader)

        if cls.__name__ == "Rectangle":
            keys_list = ['id', 'width', 'height', 'x', 'y']
        else:
            keys_list = ['id', 'size', 'x', 'y']

        result = []

        for item in csv_list:
            csv_dict = {}
            for kv in enumerate(item):
                csv_dict[keys_list[kv[0]]] = int(kv[1])
            result.append(csv_dict)

        ins_list = []

        for index in range(len(result)):
            ins_list.append(cls.create(**result[index]))

        return ins_list
