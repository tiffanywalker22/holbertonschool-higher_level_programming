-- script lists all genres contained in hbtn_0d_tvshows and displays the number of shows linked to each
SELECT tv_genres.name
FROM tv_shows
JOIN tv_shows_genres ON tv_shows.id = tv_shows_genres.show_id
JOIN tv_genres ON tv_shows_genres.genre_id = tv_genres.id
WHERE tv_shows.title = "Dexter"
ORDER BY tv_genres.name;
