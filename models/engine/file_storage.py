#!/usr/bin/python3

import json
import os


class FileStorage:
    """class that stores objects in jason"""

    __file_path: str = os.path.join(
        os.getcwd(), "models", "engine", "files", "file.json"
    )
    __objects: dict = {}

    def all(self) -> dict:
        """generates dictionary
        The dictionary is for all objects in __objects

        return: dict of objects
        """
        return self.__objects

    def new(self, obj) -> None:
        """Add new object to __object
        args:
            obj: the new object
        """
        key = str(obj.__class__.__name__) + "." + obj.id
        self.__objects[key] = obj.to_dict()

    def save(self) -> None:
        """Saves all objects
        It saves all objects in __object into json file
        """
        with open(self.__file_path, "w") as afl:
            json.dump(self.__objects, afl, indent=4)

    def reload(self) -> None:
        """loads all obhects into __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as rfl:
                self.__objects = json.load(rfl)
