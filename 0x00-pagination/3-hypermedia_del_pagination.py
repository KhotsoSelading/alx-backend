#!/usr/bin/env python3
"""
Topic: Pagination
Name: Khotso Selading
Date: 22-01-2024
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Get hypermedia index for pagination.

        Args:
            index (int): The current start index of the return page.
                         Defaults to None (starts from the beginning).
            page_size (int): The current page size. Defaults to 10.

        Returns:
            Dict: Dictionary with the following key-value pairs:
                index: the current start index of the return page.
                next_index: the next index to query with.
                page_size: the current page size.
                data: the actual page of the dataset.

        Requirements/Behavior:
            - Use assert to verify that index is in a valid range.
            - If the user queries index 0, page_size 10, they will get rows
            indexed 0 to 9 included.
            - If they request the next index (10) with page_size 10, but rows
              3,6, and 7 were deleted, the user should still receive rows
              indexed 10 to 19 included.
        """
        assert index is None or (index >= 0 and index < len(self.dataset())),
        "Invalid index"

        if index is None:
            index = 0

        next_index = index + page_size

        if next_index > len(self.dataset()):
            next_index = len(self.dataset())

        current_page = self.dataset()[index:next_index]

        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": current_page
        }
