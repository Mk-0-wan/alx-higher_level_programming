-- First create a new table with only the dexter genres
CREATE TABLE IF NOT EXISTS dex_genre AS (
	SELECT tv_genres.id, tv_genres.name
	FROM tv_genres
	INNER JOIN tv_show_genres
	ON tv_genres.id = tv_show_genres.genre_id
		INNER JOIN tv_shows
		ON tv_shows.id = tv_show_genres.show_id
		WHERE tv_shows.title = 'Dexter');
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN dex_genre
ON dex_genre.id = tv_genres.id
WHERE dex_genre.id is NULL
ORDER BY tv_genres.name;
