#!/usr/bin/env python3
"""
BasicCache Module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class
    """
    def put(self, key, item):
        """put new elemnt in cache
        """
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """get an element of cache
        """
        return self.cache_data.get(key)
