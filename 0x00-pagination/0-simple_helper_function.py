#!/usr/bin/env python3
"""
Return page index
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    returns page index
    """
    return ((page - 1) * page_size, (page * page_size))
