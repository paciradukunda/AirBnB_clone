from uuid import uuid4
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        created_at = self.created_at.fromisoformat("2017-06-14T22:31:03.285259")
        updated_at = self.updated_at.fromisoformat("2017-06-14T22:31:03.285259")
        return {
            "class_name": __class__.__name__,
            "id": self.id,
            "created_at": created_at,
            "updated_at": updated_at,
        }
