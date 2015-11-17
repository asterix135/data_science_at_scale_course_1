# Matrix multiplication in SQL

.open matrix.db as matrix;

# A(row_num, col_num, value)
# B(row_num, col_num, value)
# sum of element-wise A1 row x element-wise B1 column = 1,1
# then element-wise A1 x element-wise B2 = 1,2
# etc


SELECT a.row_num AS new_row,
        b.col_num AS new_col,
        SUM(a.value * b.value) AS new_val
    FROM a, b
    WHERE a.col_num = b.row_num
    GROUP BY a.row_num, b.col_num
    HAVING new_row = 2 AND new_col = 3;


SELECT new_val FROM
    (SELECT a.row_num AS new_row,
            b.col_num AS new_col,
            SUM(a.value * b.value) AS new_val
        FROM a, b
        WHERE a.col_num = b.row_num
        GROUP BY a.row_num, b.col_num
        HAVING new_row = 2 AND new_col = 3);
