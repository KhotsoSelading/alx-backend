#!/usr/bin/env python3
"""
Topic: Catching
Name: Khotso Selading
Date: 30-01-2024
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    class MRUCache that inherits
    from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        Initialize the class with the parent's init method
        """
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """
        Assigns the item value of the key to the dictionary self.cache_data """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.usage[-1]))
                del self.cache_data[self.usage[-1]]
                del self.usage[-1]
            if key in self.usage:
                del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Returns the value linked to a given key, or None """
        if key is not None and key in self.cache_data.keys():
            del self.usage[self.usage.index(key)]
            self.usage.append(key)
            return self.cache_data[key]
        return None


if __name__ == "__main__":
    mru_cache = MRUCache()
    mru_cache.put("A", "Hello")
    mru_cache.put("B", "World")
    mru_cache.put("C", "Holberton")
    mru_cache.put("D", "School")
    mru_cache.print_cache()
    print(mru_cache.get("B"))
    mru_cache.put("E", "Battery")
    mru_cache.print_cache()
    mru_cache.put("C", "Street")
    mru_cache.print_cache()
    print(mru_cache.get("A"))
    print(mru_cache.get("B"))
    print(mru_cache.get("C"))
    mru_cache.put("F", "Mission")
    mru_cache.print_cache()
    mru_cache.put("G", "San Francisco")
    mru_cache.print_cache()
    mru_cache.put("H", "H")
    mru_cache.print_cache()
    mru_cache.put("I", "I")
    mru_cache.print_cache()
    mru_cache.put("J", "J")
    mru_cache.print_cache()
    mru_cache.put("K", "K")
    mru_cache.print_cache()
