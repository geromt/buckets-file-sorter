# Buckets - File Sorter

CLI application to take several files in one single directory and separate them in other directories within the original 
one based on the number of files.

## Install

```commandline
make
```

## Usage
```commandline
buckets <number_of_files>
```

Example
```commandline
buckets 20
```
Separate the files in the current directory in directories each one at most have 20 files.

## Uninstall
```commandline
make clean
```