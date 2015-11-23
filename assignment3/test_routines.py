"""
Test routines for assignment 3 problems
"""

import inverted_index as ii
import MapReduce

mr = MapReduce.MapReduce()


def test_inverted_index():
    inputdata = open('data/books.json')
    mr.execute(inputdata, ii.mapper, ii.reducer)


def test_master():
    test_inverted_index()


if __name__ == '__main__':
    test_master()