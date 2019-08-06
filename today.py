#!/usr/bin/env python3
from __future__ import print_function
import os


def reversed_lines(file):
    """Generate the lines of file in reverse order."""
    part = ''
    for block in reversed_blocks(file):
        for c in reversed(block):
            if c == '\n' and part:
                yield part[::-1]
                part = ''
            part += c
    if part: yield part[::-1]


def reversed_blocks(file, blocksize=4096):
    """Generate blocks of file's contents in reverse order."""
    file.seek(0, os.SEEK_END)
    here = file.tell()
    while 0 < here:
        delta = min(blocksize, here)
        here -= delta
        file.seek(here, os.SEEK_SET)
        yield file.read(delta)


def main():
    from itertools import islice
    import datetime
    import dateutil.parser
    import humanize
    with open(os.path.expanduser('~/.chronodb'), 'r') as file:
        now = datetime.datetime.now(datetime.timezone.utc)
        today = datetime.timedelta(hours=7)
        arr = None
        dep = now
        for line in islice(reversed_lines(file), 10):
            res = line.strip().split(',', 1)
            date = dateutil.parser.parse(res[0])
            if date.day == now.day:
                if res[1] == 'arrive':
                    if arr is not None:
                        raise Exception('Missing depart, at {} and found {}'.format(arr, res[1]))
                    elif dep is None:
                        if arr is None:
                            arr = date
                            continue
                        raise Exception('Missing depart for arrive, at {} and found {}'.format(arr, res[0]))
                    arr = date
                    today -= dep - arr
                    dep = None
                elif res[1] == 'depart':
                    if dep is not None and dep is not now:
                        raise Exception('Missing arrive, at {} and found {}'.format(dep, res[0]))
                    dep = date
                    arr = None
        print(humanize.naturaldelta(today), end='')


if __name__ == '__main__':
    main()
