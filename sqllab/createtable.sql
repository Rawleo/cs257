DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quakeDate text,
  latitude float,
  longitude float,
  depth float,
  magnitude float,
  magnitudeType text,
  id text,
  locationSource char 
);