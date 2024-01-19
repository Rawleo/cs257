DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quakeDate date,
  latitude real,
  longitude float,
  depth float,
  magnitude float,
  magnitudeType text,
  id text,
  locationSource text 
);

