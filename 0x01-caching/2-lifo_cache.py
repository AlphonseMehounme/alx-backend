#!/usr/bin/env python3
"""
LIFOCache Module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class
    """
    def __init__(self):
        """Initiate and element
        """
        super().__init__()

    def put(self, key, item):
        """
        Add new element to cache
        """
        if key is not None and item is not None:
            self.cache_data.update({key: item})
            if len(self.cache_data) > LIFOCache.MAX_ITEMS:
                kd = list(self.cache_data.keys())[len(self.cache_data) - 2]
                print("DISCARD:", kd)
                del self.cache_data[kd]

    def get(self, key):
        """
        return element with key key
        """
        return self.cache_data.get(key)
