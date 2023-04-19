#!/usr/bin/env python3
"""
Module - basic_cache
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Class BasicCache"""
    def __init__(self):
        """initialize super method"""
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary self.cache_data
        the item value for the key key"""
        self.key = key
        self.item = item
        self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        self.key = key
        if key in self.cache_data:
            return self.cache_data.get(key)
        else:
            return self.cache_data.get(None)
