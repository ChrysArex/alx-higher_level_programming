-- script that lists all shows from hbtn_0d_tvshows_rate by their rating
-- The database name will be passed as an argument of the mysql command
SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating FROM tv_show_ratings JOIN tv_shows ON tv_shows.id = tv_show_ratings.show_id GROUP BY show_id ORDER BY rating DESC;
