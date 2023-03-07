#!/usr/bin/python3

import json


class FileStorage:
    """class that stores objects in jason"""

    __file_path: str = (
        "/home/pacifique/Desktop/alx/AirBnB_clone/models/engine/files/file.json"
    )
    __objects: dict = {}

    def all(self) -> dict:
        """generates dictionary
        The dictionary is for all objects in __objects

        return: dict of objects
        """
        print(" all objects")
        # return FileStorage.__objects

    def new(self, obj) -> None:
        """Add new object to __object
        args:
            obj: the new object
        """
        print("new object")
        # key = str(obj.__class__.__name__) + obj.id
        # FileStorage.__objects[key] = obj

    def save(self) -> None:
        """Saves all objects
        It saves all objects in __object into json file
        """
        print("saving to file")
        # with open(self.__file_path, "a") as afl:
        #     json.dump(afl, self.__objects)

    def reload(self) -> None:
        """loads all obhects into __objects"""
        print("reloading objets")
        # with open(self.__file_path, "r") as rfl:
        #     if rfl == None:
        #         return None
        #     else:
        #         self.__objects = json.loads(rfl.readline())
