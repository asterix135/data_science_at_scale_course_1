import MapReduce
import sys

"""
Assume you have two matrices A and B in a sparse matrix format, where each
record is of the form i, j, value. Design a MapReduce algorithm to compute the
matrix multiplication A x B

Map Input

The input to the map function will be a row of a matrix represented as a list.
Each list will be of the form [matrix, i, j, value] where matrix is a string
and i, j, and value are integers.

The first item, matrix, is a string that identifies which matrix the record
originates from. This field has two possible values: "a" indicates that the
record is from matrix A and "b" indicates that the record is from matrix B.

Reduce Output

The output from the reduce function will also be a row of the result matrix
represented as a tuple. Each tuple will be of the form (i, j, value) where each
element is an integer.

You can test your solution to this problem using matrix.json:

$ python multiply.py matrix.json

You can verify your solution by comparing your result with the file
multiply.json.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
    """
    Matrix size has to be hard-coded @ 5x5 for both for this to work
    A has dimensions L,M
    B has dimensions M,N
    for each element (i,j) of A, emit ((i,k),A[i,j] for k in 1 .. N
    for each element (j,k) of B, emit ((i,k),B[j,k] for i in 1 .. L
    :param record:
    :return:
    """
    # key: personA
    # value: personB
    for idx in range(5):
        if record[0] == 'a':
            mr.emit_intermediate((record[1], idx), record)
        else:
            mr.emit_intermediate((idx, record[2]), record)



def reducer(key, list_of_values):
    """
    One reducer per output cell
    Emit:
    key = (i,k)
    value = Sum(j) (A[i,j] * B[j,k])
    :param key:
    :param list_of_values:
    :return:
    """
    # key: word
    # value: list of occurrence counts
    cell_total = 0
    for i in range(5):
        mult1, mult2 = 0, 0
        for v in list_of_values:
            if v[0] == 'a' and v[2] == i:
                mult1 = v[3]
            elif v[0] == 'b' and v[1] == i:
                mult2 = v[3]
        cell_total += mult1 * mult2
    mr.emit((key[0], key[1], cell_total))


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
