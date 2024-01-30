#!/usr/bin/env python3
"""
Topic: Catching
Name: Khotso Selading
Date: 30-01-2024
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache defines a FIFO caching system
    """

    def __init__(self):
        """ Initialize the class with the parent's init method """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Assigns the item value for the key to the dictionary self.cache_data
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return key

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                item_discarded = self.key_indexes.pop(0)
                del self.cache_data[item_discarded]
                print("DISCARD:", item_discarded)

            self.cache_data[key] = item
            self.key_indexes.append(key)

    def get(self, key):
        """
        Returns the value linked to the given key, or None
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
