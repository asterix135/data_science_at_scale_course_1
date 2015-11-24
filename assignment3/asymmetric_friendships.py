import MapReduce
import sys

"""
The relationship "friend" is often symmetric, meaning that if I am your friend,
you are my friend. Implement a MapReduce algorithm to check whether this
property holds. Generate a list of all non-symmetric friend relationships.

Map Input

Each input record is a 2 element list [personA, personB] where personA is a
string representing the name of a person and personB is a string representing
the name of one of personA's friends. Note that it may or may not be the case
that the personA is a friend of personB.

Reduce Output

The output should be all pairs (friend, person) such that (person, friend)
appears in the dataset but (friend, person) does not.

You can test your solution to this problem using friends.json:

$ python asymmetric_friendships.py friends.json

You can verify your solution by comparing your result with the file
asymmetric_friendships.json.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
    # key: personA
    # value: personB
    key = record[0]
    # value = record[1]
    mr.emit_intermediate(key, 1)


def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    for v in list_of_values:
        total += v
    mr.emit((key, total))


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
