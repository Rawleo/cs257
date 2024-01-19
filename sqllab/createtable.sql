DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quakeDate text,
  latitude double,
  longitude double,
  depth double,
  magnitude double,
  magnitudeType text,
  id text,
  locationSource char 
);