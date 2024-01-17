DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  latitude float,
  longitude float,
  depth float,
  magnitude float,
  magnitudeType text,
  id text,
  locationSource text
);