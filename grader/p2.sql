SELECT Album.Title AS album_title, Track.TrackId AS track_id, Track.Name AS track_name, 
cast(round(Track.Milliseconds/60000) AS INTEGER) AS minutes, CAST((ROUND(CAST((Track.Milliseconds) AS REAL)/1000)-round(Track.Milliseconds/60000)*60)AS INTEGER) AS seconds 
FROM track
JOIN Album USING (AlbumId)
WHERE Album.Title = "Live [Disc 1]" or Album.Title= "Live [Disc 2]"
ORDER BY
Track.TrackID ASC