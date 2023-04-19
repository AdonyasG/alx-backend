#!/usr/bin/env python3
"""
Module - lru_cache
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU implementation"""
    def __init__(self):
        """initialization"""
        super().__init__()
        self.lru_keys = []

    def put(self, key, item):
        """
        Add a new key/value pair to the cache.
        If the number of items in the cache exceeds
        the MAX_ITEMS value,
        discard the least recently used item (LRU algorithm).

        Args:
            key: key to be added to the cache
            item: item to be added to the cache
        """
        if key is None or item is None:
            return

        # add the key to the end of the list to indicate it was recently used
        if key in self.cache_data:
            self.lru_keys.remove(key)
        self.lru_keys.append(key)

        # add the item to the cache dictionary
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            lru_key = self.lru_keys.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

    def get(self, key):
        """"
        Get the value of a given key from the cache.

        Args:
            key: key whose value is to be returned

        Returns:
            Value of the given key if it exists in the cache, otherwise None.
        """
        if key is None or key not in self.cache_data:
            return None

        # move the key to the end of the list to indicate it was recently used
        self.lru_keys.remove(key)
        self.lru_keys.append(key)

        # return the item associated with the key
        return self.cache_data[key]
