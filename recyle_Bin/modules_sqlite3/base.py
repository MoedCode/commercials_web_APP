#!/usr/bin/env python3
from Market import db
from datetime import datetime
import uuid



time = "%Y-%m-%dT%H:%M:%S.%f"


class Base():
    __tablename__ = 'base'
    id = db.Column(db.String(length=40), nullable=False, unique=True, primary_key=True)
    created_at = db.Column(db.String(length=25), nullable=False)
    updated_at = db.Column(db.String(length=25), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def to_dict(self, save_fs=None):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            # new_dict["created_at"] = new_dict["created_at"].strftime(time)
            new_dict["created_at"] = new_dict["created_at"]
        if "updated_at" in new_dict:
            # new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
            new_dict["updated_at"] = new_dict["updated_at"]
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict

    def save(self, save_option="both"):
        self.updated_at = datetime.utcnow().strftime(time)
        if save_option in ["local", "both"]:
            from modules.engine.local_storage import LocalStorage
            local_storage = LocalStorage()
            local_storage.add(self)
            local_storage.commit()
        if save_option in ["DB", "both"]:
            db.session.add(self)
            db.session.commit()

