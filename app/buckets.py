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

import argparse
import sys

from organizer import *

# Configuration of the parser
parser = argparse.ArgumentParser(description="Separate the files into directories",
                                 prog="buckets")
opt_args = parser.add_mutually_exclusive_group()
opt_args.add_argument("-n", "--number", type=int,
                      help="Max number of files in each directory")
opt_args.add_argument("-d", "--date", type=str, choices=["d", "m", "y"],
                      help="Separate the files by day, month or year")
opt_args.add_argument("-r", "--reverse",
                      help="Takes the files in the directories in the working dir, and move them to working dir",
                      action="store_true")

parser.add_argument("-p", "--prefix", default="",
                    help="Sets a prefix to the directories created")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="Displays more information")


def main():
    args = parser.parse_args()
    if args.number:
        if args.verbose:
            print("Separating by number of files")
            print(f"At most {args.number} in each directory")
        create_dirs(separate_by_number(args.number), prefix=args.prefix,
                    verbose=args.verbose)
    elif args.date:
        if args.verbose:
            print("Separating by date of last modification")
            print(f"Mode: {args.date}")
        create_dirs(separate_by_date(args.date), prefix=args.prefix,
                    key_are_int=False, verbose=args.verbose)
    elif args.reverse:
        join_from_dirs(verbose=args.verbose)
    else:
        print("Error: You must select an option")
        print("Use buckets --help to see the options available")
        sys.exit(1)


if __name__ == "__main__":
    main()
