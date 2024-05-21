#!/usr/bin/env python3
"""
Contains the FileStorage class for the Commercial Web Application project
"""

import json
import uuid
from modules.base_module import BaseModules
from modules.product import Product
import inspect
DEBUG = f"File: {inspect.currentframe().f_code.co_filename}, Line: {inspect.currentframe().f_lineno}"

# Mapping class names to actual class objects
classes = {"BaseModules": BaseModules, "Product": Product}

class FileStorage:
    """Serializes instances to a JSON file and deserializes back to instances"""

    # String - path to the JSON file
    __file_path = "data.json"
    # Dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self, cls=None):
        """Returns the dictionary __objects"""
        if cls is not None:
            # if class not passed return a empty dictionary
            new_dict = {}
            # self is instance from FileStorage file_storage = FileStorage.reload()
            # which is all instances from data file cashed in for  availability of  processing on it
            # this cashed data passed to all() method throw parameter self  when called on FileStorage
            for key, value in self.__objects.items():

                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + str(obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
            print(json_objects)

        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)


    def reload(self):
        """deserializes the JSON file to __objects"""
        print("alah yl3nk0]")
        print(self.__file_path)
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
                print("alah yl3nk[1]")
            print("alah yl3nk[2]")
            for key in jo:
                print("jsObjName=>",key["nme"])
                concern_cls = classes[jo[key]["__class__"]]
                print(concern_cls.isAClass)
                self.__objects[key] =concern_cls(**jo[key])

        except:
            pass

    def delete(self, obj=None):
        """Delete obj from __objects if it’s inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + str(obj.id)
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """Call reload() method for deserializing the JSON file to objects"""
        self.reload()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID,
        or None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = self.all(cls)
        for value in all_cls.values():
            if str(value.id) == str(id):
                return value

        return None

    def count(self, cls=None):
        """
        Count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for class_obj in all_class:
                count += len(self.all(class_obj).values())
        else:
            count = len(self.all(cls).values())

        return count
if __name__ == "__main__":
      # Create an instance of FileStorage
             # Call the reload method on the instance
    fileStorage = FileStorage()
    fileStorage.reload()
    AllStorage = fileStorage.all(Product)
    print(AllStorage)
