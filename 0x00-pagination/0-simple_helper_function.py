#!/usr/bin/env python3
"""simple_helper_fun"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return the start and end indexes for the current page.
    Args:
        page : The current page number (1-indexed).
        page_size : The number of items to display per page.

    Returns:
        tuple : A tuple containing the start and end indexes
        for the current page.
    """
    start_index: int = (page - 1) * page_size
    end_index: int = start_index + page_size
    return (start_index, end_index)
