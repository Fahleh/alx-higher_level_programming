-- Creates a database 'hbtn_0d_usa' if it doesn't exist.
-- Creates a table 'cities' with id, state-id and name, which can't be null.
-- The id is also unique, auto-generated and is also the primary key.
-- State-id must be a FOREIGN KEY that references the id of the states table.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    UNIQUE(id),
    FOREIGN KEY(state_id)
        REFERENCES states(id)
);
