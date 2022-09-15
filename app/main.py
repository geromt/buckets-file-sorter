#!/usr/bin/python3

import argparse
import sys

import organizer

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--number", type=int, help="Max number of files in each directory")
parser.add_argument("-d", "--date", type=str, help="Separate the files by day, month or year")
parser.add_argument("-p", "--prefix", help="Sets a prefix to the directories created")
parser.add_argument("-r", "--reverse",
                    help="Takes the files in the directories in the working dir, and move them to working dir",
                    action="store_true")


def main():
    args = parser.parse_args()
    if args.number:
        if args.prefix:
            organizer.create_dirs(organizer.separate_by_number(args.number),
                                  prefix=args.prefix)
        else:
            organizer.create_dirs(organizer.separate_by_number(args.number))
    elif args.date:
        if args.date in ("y", "d", "m"):
            organizer.create_dirs(organizer.separate_by_date(args.date),
                                  key_are_int=False)
        else:
            print("Error: The value is not valid.")
            print("Use buckets --help to see the valid values.")
            sys.exit(1)
    elif args.reverse:
        organizer.join_from_dirs()
    else:
        print("Error: You must select an option")
        print("Use buckets --help to see the options available")
        sys.exit(1)


if __name__ == "__main__":
    main()
