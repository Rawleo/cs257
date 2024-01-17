DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quakeDate date,
  latitude real,
  longitude real,
  depth real,
  magnitude real,
  magnitudeType text,
  id text,
  locationSource text
);