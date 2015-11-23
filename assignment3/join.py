import MapReduce
import sys

"""
Implement a relational join as a MapReduce query

Consider the following query:

SELECT *
FROM Orders, LineItem
WHERE Order.order_id = LineItem.order_id

Your MapReduce query should produce the same result as this SQL query executed
against an appropriate database.

You can consider the two input tables, Order and LineItem, as one big
concatenated bag of records that will be processed by the map function record
by record.

Map Input

Each input record is a list of strings representing a tuple in the database.
Each list element corresponds to a different attribute of the table

The first item (index 0) in each record is a string that identifies the table
the record originates from. This field has two possible values:

"line_item" indicates that the record is a line item.
"order" indicates that the record is an order.
The second element (index 1) in each record is the order_id.

LineItem records have 17 attributes including the identifier string.

Order records have 10 elements including the identifier string.

Reduce Output

The output should be a joined record: a single list of length 27 that contains
the attributes from the order record followed by the fields from the line item
record. Each list element should be a string.

You can test your solution to this problem using records.json:

$ python join.py records.json
You can can compare your solution with join.json.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
    # key: tuple of table & order_id
    # value: entire record
    key = record[1]
    mr.emit_intermediate(key, record)


def reducer(key, list_of_values):
    # key: tuple of table & order_id
    # value: merged list of all fields
    for v in list_of_values:
        if v[0] == 'order':
            for w in list_of_values:
                if w[0] == 'line_item':
                    mr.emit(v + w)


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
