-- Selects records from one table (cities) that can be found in
-- another table in the database.
-- Result must be sorted in ascending order by cities.id.
SELECT id, name FROM cities
    WHERE state_id IN
    (
        SELECT id FROM states
            WHERE name = 'California'
    )
    ORDER BY id ASC;
