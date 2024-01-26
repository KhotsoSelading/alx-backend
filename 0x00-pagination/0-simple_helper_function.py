#!/usr/bin/env python3
"""
Topic: Pagination
Name: Khotso Selading
Date: 22-01-2024
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Takes 2 integer arguments and returns a tuple of size two
    containing the start and end index corresponding to the range of
    indexes to return in a list for those pagination parameters
    Args:
        - page: Integer representing the page number (1-indexed).
        - page_size: Integer representing the number of items per page.
    Return:
        tuple(start_index, end_index)
    """
    if page <= 0 or page_size <= 0:
        raise ValueError("Page and page_size must be positive integers.")

    start_index = (page - 1) * page_size
    end_index = page * page_size

    return start_index, end_index
