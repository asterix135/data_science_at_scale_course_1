# Coded for sqlite3

.open reuters.db as reuters;

# Part a
SELECT COUNT(*) FROM Frequency
    WHERE docid = '10398_txt_earn';

# Part b
SELECT COUNT(*) FROM Frequency
    WHERE docid = '10398_txt_earn'
        AND count = 1;

# Part c
SELECT COUNT(DISTINCT(term)) FROM Frequency
    WHERE (docid = '10398_txt_earn'
        AND count=1)
    OR (docid = '925_txt_trade'
        AND count = 1);

# Part d
SELECT COUNT(DISTINCT(docid)) FROM Frequency
    WHERE term = 'law' OR term = 'legal';

# Part e
# try 0
SELECT DISTINCT(docid), SUM(count) FROM Frequency
    GROUP BY docid;

# step 1
SELECT DISTINCT(docid) FROM Frequency
    GROUP BY docid
    HAVING sum(count) > 300;

# fail
SELECT COUNT(distinct(docid)) FROM Frequency
    WHERE docid IN
        (SELECT DISTINCT(docid)
            FROM Frequency
            GROUP BY docid
            HAVING sum(count) > 300);

# Also fail - same as above
CREATE TABLE Temp AS
    SELECT DISTINCT(docid) FROM Frequency
        GROUP BY docid
        HAVING sum(count) > 300;
SELECT COUNT(*) FROM Temp;
DROP TABLE Temp;

# According to the forums, the grader does not want duplicates...

SELECT COUNT(DISTINCT(docid)) FROM
    (SELECT docid, SUM(count) AS term_count
            FROM Frequency
            GROUP BY docid
            HAVING COUNT(count) > 300);

