#!/usr/bin/env python

import collections

from pympler.classtracker import ClassTracker

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line(object):
    def __init__(self, line_number, text):
        self.line_number = line_number
        self.text = text

def get_point(i):
    return Point(i, i)

def get_line(i):
    return Line(i, "some random text" * 100)

def main():
    tracker = ClassTracker()
    tracker.track_class(Point)
    tracker.track_class(Line)
    tracker.create_snapshot()

    points = [get_point(i) for i in xrange(100000)]
    lines = [get_line(i) for i in xrange(10000)]

    tracker.create_snapshot()
    tracker.stats.print_summary()

if __name__ == "__main__":
    main()
