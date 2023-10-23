-- script that uses hbtn_0d_tvshows database to list all genres of the show Dexter
SELECT tv_genres.name
FROM tv_shows
JOIN tv_shows_genres ON tv_shows.id = tv_shows_genres.show_id
JOIN tv_genres ON tv_shows_genres.genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name;
