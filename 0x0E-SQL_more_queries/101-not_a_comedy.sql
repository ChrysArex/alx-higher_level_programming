-- script that lists all shows without the genre Comedy in  hbtn_0d_tvshows
-- The database name will be passed as an argument of the mysql command
SELECT title FROM tv_shows WHERE id NOT IN (SELECT tv_show_genres.show_id FROM tv_show_genres JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id WHERE name = "Comedy") ORDER BY title ASC;
