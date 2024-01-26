#!/usr/bin/env python3
"""
Topic: Pagination
Name: Khotso Selading
Date: 22-01-2024
"""

import csv
import math
from typing import List, Dict

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Reads from csv file and returns the dataset.
        Returns:
            List[List]: The dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def assert_positive_integer_type(value: int) -> None:
        """
        Asserts that the value is a positive integer.
        Args:
            value (int): The value to be asserted.
        """
        assert type(value) is int and value > 0

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Takes 2 integer arguments then returns requested page from the dataset
        Args:
            page (int): required page number. Should be a positive integer
            page_size (int): number of records per page. Should be a positive
                            integer
        Return:
            list of lists containing required data from the dataset
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        dataset = self.dataset()
        data_length = len(dataset)
        try:
            index = index_range(page, page_size)
            return dataset[index[0]:index[1]]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Retrieve hyperlinked information for a specific page in the dataset.

        Parameters:
        - total_pages: Integer representing the page number (1-indexed).

        Returns:
        - Dictionary containing hyperlinked information:
            - page_size: The length of the returned dataset page.
            - page: The current page number.
            - data: The dataset page (equivalent to the return from get_page).
            - next_page: Number of the next page, None if no next page.
            - prev_page: Number of the previous page, None if no previous page.
            - total_pages: The total number of pages in the dataset as an
            integer.
        """
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": page + 1 if page + 1 <= total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
