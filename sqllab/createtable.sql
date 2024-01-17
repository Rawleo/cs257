DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  "time" time with time zone,
  latitude real,
  longitude real,
  depth real,
  mag real,
  mag real,
  magType text,
  id text,
  locationSource text
);