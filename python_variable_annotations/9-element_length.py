#!/usr/bin/env python3
"""Module that provides a function to compute element lengths."""

from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """Return a list of tuples containing each string and its length.

    Args:
        lst (List[str]): A list of strings.

    Returns:
        List[Tuple[str, int]]: A list of tuples where each tuple contains
        a string and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
