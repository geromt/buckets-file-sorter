import math
import os


def separate_by_number(n: int):
    """Returns a dictionary in which each key is an integer, and it's associated with a list of file names which
    at most n elements"""
    buckets = {}
    count = 0
    index = 0
    for entry in os.scandir():
        if count == n:
            count = 0
            index += 1

        if entry.is_dir():
            continue

        if index in buckets:
            buckets[index].append(entry.name)
        else:
            buckets[index] = [entry.name]

        count += 1

    return buckets


def join_from_dirs():
    """Move all the files from all the directories into the current directory"""
    for entry in os.scandir():
        if entry.is_dir():
            for e in os.scandir(entry.path):
                os.rename(e.path, "./" + e.name)


def create_dirs(buckets, prefix=""):
    """Given a dictionary of int:list_of_file_name pairs, creates a directory for each key and move the files
    in the list to that directory"""
    for name in buckets:
        dir_name = form_name(name, len(buckets), prefix)
        os.mkdir(dir_name)
        for f in buckets[name]:
            os.rename("./" + f, "./" + dir_name + "/" + f)


def form_name(index, total, prefix):
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