"""
Test routines for assignment 3 problems
"""

import inverted_index as ii
import join

def test_inverted_index():
    inputdata = open('data/books.json')
    ii.mr.execute(inputdata, ii.mapper, ii.reducer)


def test_join():
    inputdata = open('data/records.json')
    join.mr.execute(inputdata, join.mapper, join.reducer)

def test_master():
    #test_inverted_index()
    test_join()


if __name__ == '__main__':
    test_master()