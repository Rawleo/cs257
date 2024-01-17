DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  latitude double precision,
  longitude double precision,
  depth double precision,
  magnitude double precision,
  magnitudeType text,
  id text,
  locationSource text
);