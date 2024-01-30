#!/usr/bin/env python3
"""
Topic: Catching
Name: Khotso Selading
Date: 30-01-2024
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Class LRUCache that inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """ Initialize the class with the parent's init method """
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """
        Assigns the item value of the key to the dictionary self.cache_data
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.usage[0]))
                del self.cache_data[self.usage[0]]
                del self.usage[0]
            if key in self.usage:
                del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value linked to a given key, or None
        """
        if key is not None and key in self.cache_data.keys():
            del self.usage[self.usage.index(key)]
            self.usage.append(key)
            return self.cache_data[key]
        return None


if __name__ == "__main__":
    lru_cache = LRUCache()
    lru_cache.put("A", "Hello")
    lru_cache.put("B", "World")
    lru_cache.put("C", "Holberton")
    lru_cache.put("D", "School")
    lru_cache.print_cache()
    print(lru_cache.get("B"))
    lru_cache.put("E", "Battery")
    lru_cache.print_cache()
    lru_cache.put("C", "Street")
    lru_cache.print_cache()
    print(lru_cache.get("A"))
    print(lru_cache.get("B"))
    print(lru_cache.get("C"))
    lru_cache.put("F", "Mission")
    lru_cache.print_cache()
    lru_cache.put("G", "San Francisco")
    lru_cache.print_cache()
    lru_cache.put("H", "H")
    lru_cache.print_cache()
    lru_cache.put("I", "I")
    lru_cache.print_cache()
    lru_cache.put("J", "J")
    lru_cache.print_cache()
    lru_cache.put("K", "K")
    lru_cache.print_cache()
