# Create similarity matrix

.open reuters.db as reuters;


SELECT SUM(A.count * B.count)
    FROM Frequency A, Frequency B
    WHERE A.term = B.term
        AND A.docid = '10080_txt_crude'
        AND B.docid = '17035_txt_earn'
    GROUP BY A.docid, B.docid;


# Last question

SELECT SUM(a.count * B.count)
    FROM Frequency A,
        (SELECT * FROM Frequency
         UNION
         SELECT 'q' AS docid, 'washington' as term, 1 AS count
         UNION
         SELECT 'q' AS docid, 'taxes' AS term, 1 AS count
         UNION
         SELECT 'q' as docid, 'treasury' AS term, 1 AS count) B,
    WHERE A.term = B.term
    GROUP BY docid


