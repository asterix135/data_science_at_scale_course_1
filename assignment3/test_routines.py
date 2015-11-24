"""
Test routines for assignment 3 problems
"""

import inverted_index as ii
import join
import friends
import asymmetric_friendships as af


def test_inverted_index():
    inputdata = open('data/books.json')
    ii.mr.execute(inputdata, ii.mapper, ii.reducer)


def test_join():
    inputdata = open('data/records.json')
    join.mr.execute(inputdata, join.mapper, join.reducer)


def test_friends():
    inputdata = open('data/friends.json')
    friends.mr.execute(inputdata, friends.mapper, friends.reducer)


def test_asymmetric():
    inputdata = open('data/friends.json')
    # inputdata = open('test_friends.json')

    af.mr.execute(inputdata, af.mapper, af.reducer)


def test_master():
    # test_inverted_index()
    # test_join()
    # test_friends()
    test_asymmetric()

if __name__ == '__main__':
    test_master()
