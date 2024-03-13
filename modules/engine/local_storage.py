#!/usr/bin/env python3
import json
import os
from typing import Type, Optional, Union
from hashlib import md5


class LocalStorage:
    File_Path = "Local/pro_market_data.json"
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
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__All_Dictionaries
    def add(self, Dict):
        """sets in __objects the obj with key <obj class name>.id"""
        if Dict is not None:
            key = Dict.__class__.__name__ + "." + Dict.id
            self.__All_Dictionaries[key] = Dict
    def reload_x(self):
        with open (self.File_Path, 'r') as FILE:
            Json_Objects = json.load(FILE)
            # Json_Objects = json.dumps(Json_Objects, indent=2)
            from market import Products, Base
            classes = {"Products":Products, "Base":Base}
            for key in Json_Objects:
                #obtaining the class for each object to re-insatiate
                # cause we concerning with instance not json objects
                obj_dict = Json_Objects[key]
                cls_name =obj_dict ["__class__"]
                the_class = classes[cls_name]
                print("{",f"cls_name:{cls_name},the_class:{the_class}", "}")
                print("{",f"cls_name:{type(cls_name)},the_class:{type(the_class)}", "}")
                # insatiate ech object with the class which is belongs tp
                self.__All_Dictionaries[key] = the_class(**Json_Objects[key])
    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            from market import Products, Base
            classes = {"Products":Products, "Base":Base}
            with open(self.File_Path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                print("localStorage:54")
                self.__All_Dictionaries[key] = json.loads(jo)
        except:
            pass


    def commit_x(self):
        json_objects = {}
        for key in self.__All_Dictionaries:
            if "_sa_instance_state" in key:
                del key["_sa_instance_state"]
            json_objects[key] = self.__All_Dictionaries[key].to_dict()
        with open(self.File_Path, 'w') as FILE:
            json.dump(json_objects, FILE, indent=2)
    def commit(self):
        """serializes __objects to the JSON file (path: File_Path)"""
        json_objects = {}
        for key in self.__All_Dictionaries:
            if key == "password":
                json_objects[key].decode()
            json_objects[key] = self.__All_Dictionaries[key].to_dict(save_fs=None)
        with open(self.File_Path, 'w') as f:
            json.dump(json_objects, f, indent=2)

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        from market import Products, Base
        classes = {"Products":Products, "Base":Base}
        if cls not in classes.values():
            return None
        all_cls = self.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        from market import Products, Base
        classes = {"Products":Products, "Base":Base}
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(self.all(clas).values())
        else:
            count = len(self.all(cls).values())

        return count



if  __name__ == "__main__":
    from market import Products
    product_data = {
    "name": "smart watch",
    "category": "Electronics",
    "brand": "Sample Brand",
    "price": 99.99,
    "stock_quantity": 50,
    "rating": 4.5,
    "discount": 10.0,
    "In_Stock": True,
    "barcode": "123456789",
    "description": "This is a sample product description.",
    "about": "More information about the sample product.",
    "img_list": [
        "/static/images/market/Smartwatch0.jfif",
        "/static/images/market/Smartwatch1.jfif",
        "/static/images/market/Smartwatch2.jfif"]
    }

    Prdct_inst = Products(**product_data)
    Prdct_inst2 = Products(**product_data)
    Prdct_inst3 = Products(**product_data)
    Prdct_inst4 = Products(**product_data)
    Prdct_inst5 = Products(**product_data)
    Prdct_inst6 = Products(**product_data)
    print(Prdct_inst.to_dict())
    # for key, value in Prdct_inst.to_dict().items():
    #  print(f"{key}:{value}")
    # print(Prdct_inst.__class__)
    print("/------------------------/")
    print("\________________________/")
    LS = LocalStorage()
    LS.reload()
    LS.add(Prdct_inst)
    LS.add(Prdct_inst2)
    LS.add(Prdct_inst3)
    LS.add(Prdct_inst4)
    LS.add(Prdct_inst5)
    LS.add(Prdct_inst6)
    LS.commit()

