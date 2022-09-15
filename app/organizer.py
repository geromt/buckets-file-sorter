#!/usr/bin/python3

"""This module contains functions to manage filenames and organize files

Functions:
    separate_by_number - Separate the entries in the working directory by number
    separate_by_date - Separate the entries in the working directory by date
    join_from_dirs - Move the files within the directories in working directory
        to the working directory
    create_dirs - Given a dictionary, creates a directory of each key and the
        files to that directory
"""

import math
import os
import time
from typing import Dict, List


def separate_by_number(n: int) -> Dict[int, List[str]]:
    """Separate the names of the files in the working directory by number of
    files.

    Return a dictionary in which each key is an integer, and it's associated
    with a list of file names which at most n elements

    Args:
        n: Max number of filenames in each entry.

    Returns:
        dictionary with int:List[str] pairs in which each list has n elements
        at most.
    """
    buckets = {}
    count = key = 0
    for entry in os.scandir():
        if entry.is_dir():
            continue

        if count == n:
            count = 0
            key += 1

        if key in buckets:
            buckets[key].append(entry.name)
        else:
            buckets[key] = [entry.name]

        count += 1
    return buckets


def separate_by_date(mode: str) -> Dict[str, List[str]]:
    """Separate the filenames in the working directory by date of the last
    modification.

    Returns a dictionary in which each key is an integer, and it's associated
    with a list of file names which at most n elements

    Args:
        mode: Only accepts y, m or d as possible values. Indicates if the files
            are separated by year (y), month (m) or day (d).

    Returns:
        Dictionary in which each key indicates the year, month or day of the
        filenames associated with that key

    Raises:
        ValueError: If mode's value is not y, m or d
    """
    if mode == "y":
        # This is best practice in Python, instead of assign a lambda to a
        # variable as key_name = lambda x: x.tm_year
        def key_name(x): return x.tm_year
    elif mode == "m":
        def key_name(x): return time.strftime("%Y-%m", x)
    elif mode == "d":
        def key_name(x): return time.strftime("%Y-%m-%d", x)
    else:
        raise ValueError(f"{mode} is not a valid value for mode attribute")

    buckets = {}
    for entry in os.scandir():
        if entry.is_dir():
            continue

        stat = entry.stat()
        t = time.localtime(stat.st_mtime)
        key = key_name(t)
        if key in buckets:
            buckets[key].append(entry.name)
        else:
            buckets[key] = [entry.name]

    return buckets


def join_from_dirs():
    """Move the files inside the directories in the working directory into the
     working directory. It does not delete the empty directories"""
    for entry in os.scandir():
        if entry.is_dir():
            for e in os.scandir(entry.path):
                os.rename(e.path, "./" + e.name)


def create_dirs(buckets: Dict, prefix: str = "", key_are_int: bool = True):
    """Given a dictionary of int:list_of_filename pairs, creates a directory
    for each key and move the files in the list to that directory. If the keys
    are strings you must pass the key_are_int=False value

    Args:
        buckets: Dictionary of int:list_of_filenames pairs
        prefix (optional): Prefix to name the directories that will be created
        key_are_int (optional): Indicates if the keys are of int type. If the
            value is False, the keys are taken as strings and the directories
            are named as them.
    """
    for k in buckets:
        if key_are_int:
            dir_name = _form_name(k, len(buckets), prefix)
        else:
            dir_name = k
        os.mkdir(dir_name)
        for f in buckets[k]:
            os.rename("./" + f, "./" + dir_name + "/" + f)


def _form_name(index: int, total: int, prefix="") -> str:
    """Auxiliary private function. Form a string with the same number of
    digits as total. If prefix is passed, it is added at the beginning of the
    string"""
    if total != 0:
        digits = math.floor(math.log10(total)) + 1
    else:
        digits = 1

    if index != 0:
        index_digits = math.floor(math.log10(index)) + 1
    else:
        index_digits = 1

    zeros = digits - index_digits
    return prefix + ("0" * zeros) + str(index)
