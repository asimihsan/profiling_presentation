#!/usr/bin/env python

import collections

from pympler import tracker

Point = collections.namedtuple("Point", ["x", "y"])
Line = collections.namedtuple("Line", ["line_number", "text"])

def get_point(i):
    return Point(i, i)

def get_line(i):
    return Line(i, "some random text" * 100)

def main():
    tr = tracker.SummaryTracker()

    points = [get_point(i) for i in xrange(1000000)]
    lines = [get_line(i) for i in xrange(100000)]

    tr.print_diff()

if __name__ == "__main__":
    main()
