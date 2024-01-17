DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  latitude double,
  longitude double,
  depth double,
  magnitude double,
  magnitudeType text,
  id text,
  locationSource text
);