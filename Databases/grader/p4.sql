SELECT DISTINCT Artist.name AS artist_name 
FROM Artist
JOIN Album USING (ArtistId)
JOIN Track USING (AlbumId)
JOIN PlaylistTrack USING(TrackId)
JOIN Playlist USING(PlaylistId)
WHERE Playlist.Name= "Heavy Metal Classic"
ORDER BY
Artist.name ASC