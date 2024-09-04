#!/usr/bin/env python3
"""
FIFOCache Module
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class
    """
    def put(self, key, item):
        """
        put new element in cache
        """
        if key is not None and item is not None:
            if FIFOCache.MAX_ITEMS < len(self.cache_data):

    def get(self, key):
        """
        Return an element from cach
        """
        return self.cache_data.get(key)
