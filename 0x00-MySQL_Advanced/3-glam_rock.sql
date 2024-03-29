-- lists all bands with Glam rock as their main style, ranked by their longevity
-- select statement to view longevity data
SELECT band_name, (COALESCE(split, 2022) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
