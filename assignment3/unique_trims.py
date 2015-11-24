import MapReduce
import sys

"""
Consider a set of key-value pairs where each key is sequence id and each value
is a string of nucleotides, e.g., GCTTCCGAAATGCTCGAA....

Write a MapReduce query to remove the last 10 characters from each string of
nucleotides, then remove any duplicates generated.

Map Input

Each input record is a 2 element list [sequence id, nucleotides] where
sequence id is a string representing a unique identifier for the sequence and
nucleotides is a string representing a sequence of nucleotides

Reduce Output

The output from the reduce function should be the unique trimmed nucleotide
strings.

You can test your solution to this problem using dna.json:

$ python unique_trims.py dna.json

You can verify your solution by comparing your result with the file
unique_trims.json.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
    # key: personA
    # value: personB
    # key = record[0]
    value = record[1]
    value = value[:(len(value)-10)]
    mr.emit_intermediate(value, value)


def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    mr.emit(key)


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
