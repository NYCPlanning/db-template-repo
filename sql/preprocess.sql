-- create staging versions of relvant import data to modify
DROP TABLE IF EXISTS _dcp_zoningdistricts;

CREATE TABLE _dcp_zoningdistricts AS TABLE dcp_zoningdistricts;

