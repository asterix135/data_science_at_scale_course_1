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

Note that the grader requires both (friend, person) and (person, friend)
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
    # key: personA
    # value: personB
    key = record[0]
    person_a = key
    person_b = record[1]
    mr.emit_intermediate(person_a, (person_a, person_b))
    mr.emit_intermediate(person_b, (person_a, person_b))


def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    for v in list_of_values:
        if v[0] == key:
            for w in list_of_values:
                if w[0] == v[1]:
                    list_of_values.remove((v[0], v[1]))
                    list_of_values.remove((v[1], v[0]))
    for v in list_of_values:
        mr.emit(v)


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
