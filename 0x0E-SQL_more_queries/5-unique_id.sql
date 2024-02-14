-- Creates a table 'unique_id' with id and name columns.
-- Both coulumns must not be null, and id must contain unique values.
CREATE TABLE IF NOT EXISTS unique_id(
    id INT DEFAULT 1,
    name VARCHAR(256),
    UNIQUE(id)
);
