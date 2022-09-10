import os


def separate_by_number(n: int):
    buckets = {}
    count = 0
    index = 0
    for f in os.listdir():
        if count == n:
            count = 0
            index += 1

        if index in buckets:
            buckets[index].append(f)
        else:
            buckets[index] = [f]

        count += 1

    return buckets


def create_dirs(buckets):
    for name in buckets:
        os.mkdir(str(name))
        for f in buckets[name]:
            os.rename("./" + f, "./" + str(name) + "/" + f)