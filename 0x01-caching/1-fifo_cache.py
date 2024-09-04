#!/usr/bin/env python3
"""
FIFOCache Module
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class
    """
    def __init__(self):
        """
        init method
        """
        super().__init__()

    def put(self, key, item):
        """
        put new element in cache
        """
        if key is not None and item is not None:
            self.cache_data.update({key: item})
            if len(self.cache_data) > FIFOCache.MAX_ITEMS:
                kd = list(self.cache_data.keys())[0]
                print("DISCARD:", kd)
                del self.cache_data[kd]

    def get(self, key):
        """
        Return an element from cach
        """
        return self.cache_data.get(key)
