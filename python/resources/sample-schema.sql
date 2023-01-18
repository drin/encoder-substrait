CREATE OR REPLACE TABLE expr (
     gene_id VARCHAR(32)
    ,cell_id VARCHAR(32)
    ,expr    DOUBLE
    ,PRIMARY KEY(gene_id, cell_id)
);

CREATE OR REPLACE TABLE clusters (
     metacluster_id INT
    ,cluster_id     INT
    ,cell_id        VARCHAR(32)
    ,PRIMARY KEY(metacluster_id, cluster_id, cell_id)
);
