-- ists all shows, and all genres linked to that show in hbtn_0d_tvshows
-- The database name will be passed as an argument of the mysql command
SELECT tv_shows.title, tv_genres.name FROM tv_genres JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title, tv_genres.name ASC;
