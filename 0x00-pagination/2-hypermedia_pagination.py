#!/usr/bin/env python3
"""
Topic: Pagination
Name: Khotso Selading
Date: 22-01-2024
"""

import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
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
        Returns a page of the dataset.
        Args:
            page (int): The page number.
            page_size (int): The page size.
        Returns:
            List[List]: The page of the dataset.
        """
        self.assert_positive_integer_type(page)
        self.assert_positive_integer_type(page_size)
        dataset = self.dataset()
        start, end = index_range(page, page_size)
        try:
            data = dataset[start:end]
        except IndexError:
            data = []
        return data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Retrieve hyperlinked information for a specific page in the dataset.

        Parameters:
        - page: Integer representing the page number (1-indexed).
        - page_size: Integer representing the number of items per page.

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
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        data_page = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        next_page = (
            page + 1 if page * page_size < len(self.dataset()) else None
        )
        prev_page = page - 1 if page > 1 else None

        hyper_info = {
            "page_size": len(data_page),
            "page": page,
            "data": data_page,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

        return hyper_info
