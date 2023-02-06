#!/usr/bin/python3

"""CLI application: separate the files in the working directory into different directories depending on the number of
files or the date of the last modification.

To see all options use
    buckets.py --help
"""
import os
import click

from utils import *


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
    if verbose:
        click.secho("Separate files by number")
        click.secho(f"Each directory contains at most {number} files")

    buckets_dic = separate_files_by_number(number)
    create_dirs(buckets_dic, prefix=prefix, are_keys_int=True, verbose=verbose)


@buckets.command(short_help="Separate files by date (year, month or day).")
@click.option("--prefix", required=False, default="", type=str, help="Prefix used to name the directories.")
@click.option("--verbose", "-v", is_flag=True, help="Enables verbose mode.")
@click.argument("mode", nargs=1, type=click.Choice(['y', 'm', 'd']))
def bydate(mode: str, prefix, verbose):
    """Separate the filenames in the working directory by date of the last
    modification. It can separate files by year (y), month (m) or day (d).
    """
    if verbose:
        click.echo("Separate files by date")
        click.echo(f"Mode: {mode}")

    buckets_dic = separate_files_by_date(mode)
    create_dirs(buckets_dic, prefix=prefix, are_keys_int=False, verbose=verbose)


@buckets.command(short_help="Reverse the buckets operation.")
@click.option("--verbose", "-v", is_flag=True, help="Enables verbose mode.")
@click.option("--remove", "-r", is_flag=True, help="Remove the empty directories")
def reverse(verbose=False, remove=False):
    """Move the files inside the directories in the working directory into the
     working directory. It does not delete the empty directories
     """
    if verbose:
        click.echo("Reverse buckets")

    for entry in os.scandir():
        if entry.is_dir():
            for e in os.scandir(entry.path):
                os.rename(e.path, "./" + e.name)
                if verbose:
                    click.echo(f"Move file: {entry.name + e.name} -> ./{e.name}")
            if remove:
                os.rmdir(entry)


if __name__ == "__main__":
    buckets()
