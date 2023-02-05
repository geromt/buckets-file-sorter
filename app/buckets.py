#!/usr/bin/python3

"""CLI application: separate the files in the working directory into different
directories depending on the number of files or the date of the last
modification.

To see all options use
    buckets.py --help
or
    buckets --help
after installing it
"""

import sys
import os
import click


@click.group()
def buckets():
    click.secho("*** Buckets ***", fg="blue")


@buckets.command(short_help="Separate files by number of files")
@click.option("--prefix", required=False, type=str, default="", help="Prefix used to name the directories.")
@click.option("--verbose", "-v", is_flag=True, help="Enables verbose mode.")
@click.argument("number", nargs=1, type=int)
def bynumber(number: int, prefix: str = "", verbose: bool = False):
    """Separate the names of the files in the working directory by number of
    files.

    NUMBER: Max number of filenames in each directory.
    """
    buckets_dir = {}
    count = key = 0
    for entry in os.scandir():
        if entry.is_dir():
            continue

        if count == number:
            count = 0
            key += 1

        if key in buckets_dir:
            buckets_dir[key].append(entry.name)
        else:
            buckets_dir[key] = [entry.name]

        count += 1
    create_dirs(buckets_dir, prefix=prefix, key_are_int=True, verbose=verbose)


@buckets.command(short_help="Separate files by date (year, month or day).")
@click.option("--prefix", required=False, default="", type=str, help="Prefix used to name the directories.")
@click.option("--verbose", "-v", is_flag=True, help="Enables verbose mode.")
@click.argument("mode", nargs=1, type=click.Choice(['y', 'm', 'd']))
def bydate(mode: str, prefix, verbose):
    """Separate the filenames in the working directory by date of the last
    modification. It can separate files by year (y), month (m) or day (d).
    """
    if mode == "y":
        # This is best practice in Python, instead of assign a lambda to a
        # variable as key_name = lambda x: x.tm_year
        def key_name(x): return str(x.tm_year)
    elif mode == "m":
        def key_name(x): return time.strftime("%Y-%m", x)
    elif mode == "d":
        def key_name(x): return time.strftime("%Y-%m-%d", x)
    else:
        raise ValueError(f"{mode} is not a valid value for mode attribute")

    buckets_dir = {}
    for entry in os.scandir():
        if entry.is_dir():
            continue

        stat = entry.stat()
        t = time.localtime(stat.st_mtime)
        key = key_name(t)
        if key in buckets_dir:
            buckets_dir[key].append(entry.name)
        else:
            buckets_dir[key] = [entry.name]

    create_dirs(buckets_dir, prefix=prefix, key_are_int=False, verbose=verbose)


@buckets.command(short_help="Reverse the buckets operation.")
@click.option("--verbose", "-v", is_flag=True, help="Enables verbose mode.")
def reverse(verbose=False):
    """Move the files inside the directories in the working directory into the
     working directory. It does not delete the empty directories
     """
    for entry in os.scandir():
        if entry.is_dir():
            for e in os.scandir(entry.path):
                os.rename(e.path, "./" + e.name)
                if verbose:
                    print(f"Move file: {entry.name + e.name} -> ./{e.name}")


def create_dirs(buckets: Dict, prefix: str = "", key_are_int: bool = True,
                verbose: bool = False):
    """Given a dictionary of int:list_of_filename pairs, creates a directory
    for each key and move the files in the list to that directory. If the keys
    are strings you must pass the key_are_int=False value

    Args:
        buckets: Dictionary of int:list_of_filenames pairs
        prefix (optional): Prefix to name the directories that will be created
        key_are_int (optional): Indicates if the keys are of int type. If the
            value is False, the keys are taken as strings and the directories
            are named as them.
        verbose (optional): If True, prints more information in the stdout.
    """
    for k in buckets:
        if key_are_int:
            dir_name = _form_name(k, len(buckets), prefix)
        else:
            dir_name = prefix + k
        os.mkdir(dir_name)
        if verbose:
            print(f"Create directory: {dir_name}")
        for f in buckets[k]:
            os.rename("./" + f, "./" + dir_name + "/" + f)
            if verbose:
                print(f"Move file: {f} -> {dir_name + '/' + f}")


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


if __name__ == "__main__":
    buckets()
