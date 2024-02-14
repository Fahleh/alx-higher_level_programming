-- Creates a table 'id_not_null' with id and name columns.
-- Both coulumns must not be null
CREATE TABLE IF NOT EXISTS id_not_null(
    id INT DEFAULT 1,
    name VARCHAR(256) NOT NULL
);
