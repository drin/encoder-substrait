SELECT  COALESCE(clust_1.gene_id, clust_2.gene_id)              AS gene_id
               ,(clust_1.cell_count + clust_2.cell_count)               AS pop_size
               ,(clust_1.expr_avg   - clust_2.expr_avg)                 AS pop_avg
               ,sqrt(
                    (clust_1.expr_var / CAST(clust_1.cell_count AS DOUBLE))
                  + (clust_2.expr_var / CAST(clust_2.cell_count AS DOUBLE))
                )                                                       AS pop_stddev
               ,clust_1.cell_count                                      AS left_size
               ,clust_2.cell_count                                      AS right_size

FROM   (SELECT    gene_id
                 ,COUNT(*)        AS cell_count
                 ,AVG(e.expr)     AS expr_avg
                 ,VAR_POP(e.expr) AS expr_var
        FROM     clusters c
                 JOIN  expr e
                 USING (cell_id)
        WHERE    c.metacluster_id = 12
        GROUP BY e.gene_id
        ) clust_1

        FULL OUTER JOIN (SELECT    gene_id
                                  ,COUNT(*)        AS cell_count
                                  ,AVG(e.expr)     AS expr_avg
                                  ,VAR_POP(e.expr) AS expr_var
                         FROM     clusters c
                                  JOIN  expr e
                                  USING (cell_id)
                         WHERE    c.metacluster_id = 13
                         GROUP BY e.gene_id
        ) clust_2
        USING (gene_id)

LIMIT 25
