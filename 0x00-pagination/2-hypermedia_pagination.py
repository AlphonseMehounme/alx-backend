#!/usr/bin/env python3
"""
return dataset pages
"""
import csv
import math
from typing import List, Tuple, Dict, Union


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    returns page index
    """
    return ((page - 1) * page_size, (page * page_size))


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
        """Return dataset pages
        """
        assert isinstance(page, int) and page > 0, "Must be a positive int"
        assert isinstance(page_size, int) and page_size > 0, "Must be 0+ int"
        rang = index_range(page, page_size)
        self.dataset()
        return self.__dataset[slice(*rang)]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str,
                                                                    Union[int,
                                                                          List[List],
                                                                          None]]:
        """return hypermedia page
        """
        data = self.get_page(page, page_size)
        total_pages = len(self.dataset()) / page_size
        if round(total_pages) < total_pages:
            total_pages = round(total_pages) + 1
        else:
            total_pages = round(total_pages)
        next_page = page + 1
        if page >= total_pages:
            next_page = None
        prev_page = page - 1
        if page == 1:
            prev_page = None
        mydata = {'page_size': page_size, 'page': page, 'data': data,
                  'next_page': next_page, 'prev_page': prev_page,
                  'total_pages': total_pages}
        return mydata
