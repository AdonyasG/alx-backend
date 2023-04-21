#!/usr/bin/env python3
"""simple_pagination"""
import csv
import math
from typing import List, Dict
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get page"""
        assert (isinstance(page, int))
        assert (isinstance(page_size, int))
        assert page > 0
        assert page_size > 0
        index = index_range(page, page_size)

        data = self.dataset()

        if index[1] > len(data):
            return []
        return data[index[0]:index[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, int]:
        data = self.get_page(page, page_size)
        dict = {
            'page_size': len(data),
            'page': page,
            'data': data
            }
        if page > 1:
            dict['prev_page'] = page - 1
        else:
            dict['prev_page'] = None

        return dict
