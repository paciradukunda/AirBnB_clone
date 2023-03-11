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
        self.__objects[key] = obj

    def save(self) -> None:
        """Saves all objects
        It saves all objects in __object into json file
        """
        try:
            json_dict = {
                k: (lambda x: x.to_dict())(v)
                for k, v in self.__objects.items()
            }
            with open(self.__file_path, "w") as afl:
                json.dump(json_dict, afl, indent=4)
        except AttributeError:
            print(self.__objects)

    def reload(self) -> None:
        from ..amenity import Amenity
        from ..base_model import BaseModel
        from ..city import City
        from ..place import Place
        from ..Review import Review
        from ..state import State
        from ..user import User

        """loads all obhects into __objects"""
        dict_of_cls = {
            "Amenity": Amenity,
            "BaseModel": BaseModel,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
            "User": User,
        }
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as rfl:
                loaded_obj = json.load(rfl)
            try:
                for k, v in loaded_obj.items():
                    obj_cls = dict_of_cls[v["__class__"]]
                    obj = obj_cls(**v)
                    self.__objects[k] = obj
            except KeyError as e:
                print("** Class doesn't exist **")
