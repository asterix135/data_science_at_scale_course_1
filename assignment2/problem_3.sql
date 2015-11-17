# Create similarity matrix

.open reuters.db as reuters;


SELECT SUM(A.count * B.count)
    FROM Frequency A, Frequency B
    WHERE A.term = B.term
        AND A.docid = '10080_txt_crude'
        AND B.docid = '17035_txt_earn'
    GROUP BY A.docid, B.docid;


# Last question

# Nope - but start here
SELECT A.docid, SUM(a.count * B.count) AS sim_val
    FROM Frequency A,
        (SELECT * FROM Frequency
         UNION
         SELECT 'q' AS docid, 'washington' as term, 1 AS count
         UNION
         SELECT 'q' AS docid, 'taxes' AS term, 1 AS count
         UNION
         SELECT 'q' as docid, 'treasury' AS term, 1 AS count) B
    WHERE A.term = B.term
    ORDER BY sim_val DESC LIMIT 1;


# This one works

SELECT A.docid, B.docid, SUM(A.count * B.count) as new_val
    FROM (
             SELECT * FROM Frequency
             UNION
             SELECT 'q' AS docid, 'washington' as term, 1 AS count
             UNION
             SELECT 'q' AS docid, 'taxes' AS term, 1 AS count
             UNION
             SELECT 'q' as docid, 'treasury' AS term, 1 AS count
          ) A,
          (
             SELECT * FROM Frequency
             UNION
             SELECT 'q' AS docid, 'washington' as term, 1 AS count
             UNION
             SELECT 'q' AS docid, 'taxes' AS term, 1 AS count
             UNION
             SELECT 'q' as docid, 'treasury' AS term, 1 AS count
           ) B
    WHERE A.term = B.term
        AND B.docid = 'q'
    GROUP BY A.docid, B.docid
    ORDER BY new_val DESC LIMIT 1;



