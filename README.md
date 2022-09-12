# Buckets - File Sorter

CLI application to take several files in one single directory and separate them in other directories within the original 
one given a number of files. If there are directories among the files, it ignores them. 

## Install

```commandline
make
```

## Usage

### Help
```commandline
buckets --help
```
It shows the available options.

### Separate by number of files
```commandline
buckets -n <number>
buckets --number <number>
```
Separate the files in directories each one with at most `<number>` files.

*Example*
```commandline
buckets -n 20
```
Separate the files in the current directory in directories each one at most have 20 files.

### Reverse operation
```commandline
buckets -r
buckets --reverse
```
Takes the files in the directories in the working directory, and move them to the working directory.

## Uninstall
```commandline
make clean
```