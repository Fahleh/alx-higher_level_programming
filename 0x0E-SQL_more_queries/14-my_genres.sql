-- Lists all genres of the show dexter
SELECT a.name
    FROM tv_genres a
    INNER JOIN tv_show_genres b
        ON a.id = b.genre_id
    INNER JOIN tv_shows c
        ON c.id = b.show_id
    WHERE c.title = 'Dexter'
    ORDER BY a.name ASC;
