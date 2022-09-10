import os


def separate_by_number(n: int):
    """Returns a dictionary in which each key is an integer and it's associated with a list of file names which
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


def create_dirs(buckets):
    """Given a dictionary of int:list_of_file_name pairs, creates a directory for each key and move the files
    in the list to that directory"""
    for name in buckets:
        os.mkdir(str(name))
        for f in buckets[name]:
            os.rename("./" + f, "./" + str(name) + "/" + f)