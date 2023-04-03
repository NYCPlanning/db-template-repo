ALTER TABLE _dcp_zoningdistricts ADD new_build_column text;

DROP TABLE IF EXISTS validzones;

CREATE TABLE validzones AS (
SELECT a.zonedist, ST_MakeValid(a.geom) as geom  
FROM _dcp_zoningdistricts a
WHERE ST_GeometryType(ST_MakeValid(a.geom)) = 'ST_MultiPolygon');
CREATE INDEX validzones_geom_idx ON validzones USING GIST (geom gist_geometry_ops_2d);