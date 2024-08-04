Select Album.Title AS album_title From Album 
Join Artist using(ArtistId)
WHERE Artist.name="Led Zeppelin" 
ORDER BY Album.title ASC