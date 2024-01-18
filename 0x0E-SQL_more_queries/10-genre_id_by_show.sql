-- hbtn_0d_tvshows that have at least one genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows.title INNER JOIN tv_show_genres.genre_id
ON tv_shows.id = tv_genres.genre_id
ORDER BY tv_shows.title
