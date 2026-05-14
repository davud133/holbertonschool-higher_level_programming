-- Showss films
SELECT tv_shows.title, NULL FROM tv_shows JOIN tv_show_genres ON tv_shows.id = tv_show_genres.genre_id ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
