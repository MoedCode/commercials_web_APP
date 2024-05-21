#!/usr/bin/python3
"""
initialize the models package
"""

from os import getenv
from modules.engine.File_Storage import FileStorage

storage = FileStorage()
"""

storage_t = getenv("PRO_MARKET_STORAGE_TYPE")

if storage_t == "db":
    from modules.engine.DB_Storage  import DBStorage
    storage = DBStorage()
else:
    from modules.engine.File_Storage import FileStorage
    storage = FileStorage()
storage.reload()
"""