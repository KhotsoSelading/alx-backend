#!/usr/bin/env python3
"""
Topic: Catching
Name: Khotso Selading
Date: 30-01-2024
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache inherits from BaseCaching
    Methods:
        put(key, item) - store a key-value pair
        get(key) - retrieve the value associated with a key
    """

    def __init__(self):
        """
        Initialize the class using the parent class __init__ method
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """
        Assigns item value for the key to the dictionary self.cache_data
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Returns the value linked to key. """
        return self.cache_data.get(key, None)
