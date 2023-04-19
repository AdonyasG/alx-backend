#!/usr/bin/env python3
"""
Module - fifo_cache
"""
from base_caching import BaseCaching
from queue import Queue


class FIFOCache(BaseCaching):
    """Class FIFOCache"""
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """If the number of items in
        self.cache_data is higher than BaseCaching.MAX_ITEMS:
        must discard the first item put in cache (FIFO algorithm)
        must print DISCARD: with the key discarded
        and following by a new line"""
        if key and item:
            self.cache_data[key] = item
            self.order.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            for key, val in self.cache_data.items():
                evict_key = self.order.pop(0)
                del self.cache_data[evict_key]
                print("DISCARD: {}".format(evict_key))
                break

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        return super().get(key, None)
