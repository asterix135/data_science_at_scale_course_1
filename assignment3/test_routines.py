"""
Test routines for assignment 3 problems
"""

import inverted_index as ii
import join
import friends
import asymmetric_friendships as af
import unique_trims as ut
import multiply


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


def test_unique_trims():
    inputdata = open('data/dna.json')
    ut.mr.execute(inputdata, ut.mapper, ut.reducer)


def test_multiply():
    inputdata = open('data/matrix.json')
    multiply.mr.execute(inputdata, multiply.mapper, multiply.reducer)


def test_master():
    # test_inverted_index()
    # test_join()
    # test_friends()
    # test_asymmetric()
    # test_unique_trims()
    test_multiply()


if __name__ == '__main__':
    test_master()
