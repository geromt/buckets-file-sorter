# Buckets - File Sorter

CLI application to take several files in one single directory and separate them 
in other directories within the original one given a number of files. If there 
are directories among the files, it ignores them.

This project is licensed under the terms of the [MIT license](./LICENSE).

## Install

```commandline
make
```

## Usage

### Help
```commandline
buckets --help
```
It shows the available options

### Separate by number of files
```
buckets -n <number>
buckets --number <number>
```
Separate the files in directories each one with at most `<number>` files.

You can also indicate a prefix to name the directories
```
buckets -n <number> -p <prefix>
```

**Example**
```commandline
buckets -n 20
```
Separate the files in the current directory in directories each one at most have
20 files.

### Separate by date
```
buckets -d {d,m,y}
```
Separate the files by day, month or year. The directory's name change with each 
option: 

| day     | `yyyy-mm-dd`   |
|---------|----------------|
| month   | `yyyy-mm`      |
| year    | `yyyy`         |

You can also use the prefix option along with this option

### Reverse operation
```commandline
buckets -r
buckets --reverse
```
Takes the files in the directories in the working directory, and move them to 
the working directory.

### Verbose
```commandline
buckets -v
buckets --verbose
```
Displays more information

## Uninstall
```commandline
make clean
```