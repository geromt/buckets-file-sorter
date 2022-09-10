# Buckets - File Sorter

CLI application to take several files in one single directory and separate them in other directories within the original 
one given a number of files. If there are directories among the files, it ignores them. 

## Install

```commandline
make
```

## Usage
```
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