#!/usr/bin/env python3
import json
import os
from typing import Type, Optional, Union
from hashlib import md5

class LocalStorage:

    __All_Dictionaries = {}

    def all(self, cls=None):
        """if class name is passed loop over all dictionary which loaded from
                reload method check for each dictionary  if class name passed is same as
                class name passed or not , if its assign to new_dict
            else return  __All_Dictionaries as it is
        """
        if cls is not None:
            new_dict = {}
            for key, value in self.__All_Dictionaries.items():
                if cls  == value.__class__ or cls == value.__class__.name__:
                    new_dict[key] = value
            return new_dict
    def add(self, Dict):
        """sets in __objects the obj with key <obj class name>.id"""
        if Dict is not None:
            key = Dict.__cls__.__name__ + "." + Dict.id
            self.__All_Dictionaries[key] = Dict
    def commit(self):
        json_objects = {}
        for key in self.__All_Dictionaries:
            json_objects[key] = self.__All_Dictionaries[key].to_dict()



