-- script that lists all genres in hbtn_0d_tvshows_rate by their rating.
-- The database name will be passed as an argument of the mysql command
SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating FROM tv_genres JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_show_genres.show_id GROUP BY tv_genres.id ORDER BY rating DESC;
