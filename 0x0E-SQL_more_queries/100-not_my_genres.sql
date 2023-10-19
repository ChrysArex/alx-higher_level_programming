-- lists all genres not linked to the show Dexter
-- The database name will be passed as an argument of the mysql command
SELECT tv_genres.name FROM tv_genres WHERE id NOT IN (SELECT tv_show_genres.genre_id FROM tv_shows JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id WHERE tv_shows.title = "Dexter") ORDER BY tv_genres.name ASC;
