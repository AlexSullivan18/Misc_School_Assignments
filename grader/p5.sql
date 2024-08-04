SELECT Distinct Album.title AS album_title From Album
JOIN Track USING(AlbumId)
JOIN Genre USING(GenreId)
WHERE 
Genre.Name= "Bossa Nova"