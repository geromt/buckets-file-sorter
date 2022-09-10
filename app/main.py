#!/usr/bin/python3

import sys
import sorter


def main():
    try:
        n = int(sys.argv[1])
        if n <= 0:
            print("Error: Argument must be greater or equal to 1")
            sys.exit(1)
    except IndexError:
        print("Error: Need to provide the number of files in each directory")
        sys.exit(1)
    except ValueError:
        print("Error: Argument is not a number")
        sys.exit(1)

    sorter.create_dirs(sorter.separate_by_number(n))


if __name__ == "__main__":
    main()
