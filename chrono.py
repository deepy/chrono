#!/usr/bin/env python3
from datetime import datetime, timezone
import os
import csv


def write_entry(direction):
    with open(os.path.expanduser('~/.chronodb'), 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([datetime.now(timezone.utc), direction])


def print_usage():
    print("usage: chrono.py arrive/depart")


def launch():
    import sys
    if len(sys.argv) == 2:
        if sys.argv[1].startswith("arr"):
            write_entry("arrive")
        elif sys.argv[1].endswith("dep"):
            write_entry("depart")
        else:
            print_usage()
    else:
        print_usage()

if __name__ == '__main__':
    launch()

