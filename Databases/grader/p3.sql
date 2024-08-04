SELECT 	InvoiceLine.InvoiceLineId AS invoice_line_id,
		Track.TrackId AS track_id,
		Album.Title AS album_title,
		Artist.Name AS artist_name,
		Track.name AS track_name,
		MediaType.name AS  media_type,
		printf( "$"||invoiceLine.UnitPrice) AS unit_price,
		InvoiceLine.Quantity AS qty
		FROM InvoiceLine
		JOIN Invoice USING (InvoiceId)
		JOIN Track USING (TrackId)
		JOIN MediaType USING (MediaTypeId)
		JOIN Album USING (AlbumId)
		JOIN Artist USING (ArtistId)
WHERE 
	Invoice.Total>=25
ORDER BY 
ALBUM.Title ASC, 
Artist.name ASC, 
Track.name ASC