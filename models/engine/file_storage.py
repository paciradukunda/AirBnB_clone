#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
import os


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """

    __file_path: str = os.path.join(os.getcwd(), "file.json")
    __objects: dict = {}

    def all(self) -> dict:
        """generates dictionary
        The dictionary is for all objects in __objects

        return: dict of objects
        """
        return FileStorage.__objects

    def new(self, obj) -> None:
        """Add new object to __object
        args:
            obj: the new object
        """
        key = str(obj.__class__.__name__) + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self) -> None:
        """Saves all objects
        It saves all objects in __object into json file
        """
        odict = FileStorage.__objects
        json_dict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as afl:
            json.dump(json_dict, afl)

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
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as rfl:
                loaded_obj = json.load(rfl)
                for k, v in loaded_obj.items():
                    obj_cls = dict_of_cls[v["__class__"]]
                    obj = obj_cls(**v)
                    self.__objects[k] = obj
        else:
            return
