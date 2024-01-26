#!/usr/bin/env python3
"""
Topic: Pagination
Name: Khotso Selading
Date: 22-01-2024
"""

import csv
import math
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
        """
        Retrieves a paginated subset of the dataset starting from the
        specified index.

        Args:
            index (int): The index of the first item in the current page.
            page_size (int): The desired number of records per page.

        Returns:
            Dict: A dictionary containing the following key-value pairs:
                - 'index': The current start index of the return page.
                - 'next_index': The next index to query with (index of the
                first item after the last item on the current page).
                - 'page_size': The current page size.
                - 'data': The actual page of the dataset.

        Raises:
            AssertionError: If the specified index is not within the valid
            range [0, dataset_length).
        """
        dataset = self.indexed_dataset()
        data_length = len(dataset)

        assert 0 <= index < data_length

        response = {'index': index, 'page_size': page_size}
        data = []

        for _ in range(page_size):
            while index < data_length and index not in dataset:
                index += 1

            if index < data_length:
                data.append(dataset[index])
                index += 1

        response['data'] = data
        response['next_index'] = index if index < data_length else None

        return response
