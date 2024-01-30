#!/usr/bin/env python3
"""
Topic: Catching
Name: Khotso Selading
Date: 30-01-2024
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    FIFOCache defines a FIFO caching system
    """

    def __init__(self):
        """
        Initialize the class with the parent's init method
        """
        self.order_list = {}
        super().__init__()

    def put(self, key, item):
        """ Adds an item in the cache """
        if not (key is None or item is None):
            self.cache_data[key] = item
            if len(self.cache_data.keys()) > self.MAX_ITEMS:
                pop = min(self.order_list, key=self.order_list.get)
                self.order_list.pop(pop)
                self.cache_data.pop(pop)
                print(f"DISCARD: {pop}")
            if not (key in self.order_list):
                self.order_list[key] = 0
            else:
                self.order_list[key] += 1

    def get(self, key):
        """ Returns the value linked to a given key, or None """
        if (key is None) or not (key in self.cache_data):
            return None
        self.order_list[key] += 1
        return self.cache_data.get(key)


if __name__ == "__main__":
    lfu_cache = LFUCache()
    lfu_cache.put("A", "Hello")
    lfu_cache.put("B", "World")
    lfu_cache.put("C", "Holberton")
    lfu_cache.put("D", "School")
    lfu_cache.print_cache()
    print(lfu_cache.get("B"))
    lfu_cache.put("E", "Battery")
    lfu_cache.print_cache()
    lfu_cache.put("C", "Street")
    lfu_cache.print_cache()
    print(lfu_cache.get("A"))
    print(lfu_cache.get("B"))
    print(lfu_cache.get("C"))
    lfu_cache.put("F", "Mission")
    lfu_cache.print_cache()
    lfu_cache.put("G", "San Francisco")
    lfu_cache.print_cache()
    lfu_cache.put("H", "H")
    lfu_cache.print_cache()
    lfu_cache.put("I", "I")
    lfu_cache.print_cache()
    print(lfu_cache.get("I"))
    print(lfu_cache.get("H"))
    print(lfu_cache.get("I"))
    print(lfu_cache.get("H"))
    print(lfu_cache.get("I"))
    print(lfu_cache.get("H"))
    lfu_cache.put("J", "J")
    lfu_cache.print_cache()
    lfu_cache.put("K", "K")
    lfu_cache.print_cache()
    lfu_cache.put("L", "L")
    lfu_cache.print_cache()
    lfu_cache.put("M", "M")
    lfu_cache.print_cache()
