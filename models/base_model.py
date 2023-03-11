#!/usr/bin/python3

from datetime import datetime
from uuid import uuid4
from . import storage


class BaseModel:
    """Basemodel blueprint
    args:
        id: unique identifier
        created_at: time of creation
        updated_at: time of update

    return: BaseModel object
    """

    def __init__(self, *args, **kwargs) -> None:
        """Initializes object
        args:
            *args: list of argumnets to create object
            **kwargs: list of key value armumnets to create object
        return: BaseModel object
        """

        self.id: str = str(uuid4())
        self.created_at: datetime = datetime.now()
        self.updated_at: datetime = datetime.now()

        if len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                elif k == "created_at" or k == "updated_at":
                    date_ = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                    self.__setattr__(k, date_)
                else:
                    self.__setattr__(k, v)
        else:
            storage.new(self)

    def __str__(self) -> str:
        """prints the objects details

        return: str
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self) -> None:
        """saves the object"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self) -> dict:
        """dictionary replesantation of object

        return: dictinary
        """
        new_dict = {k: v for k, v in self.__dict__.items()}
        created_at_str = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        new_dict["created_at"] = created_at_str
        updated_at_str = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        new_dict["updated_at"] = updated_at_str
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
