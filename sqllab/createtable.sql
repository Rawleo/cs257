DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quakeDate time with time zone,
  latitude real,
  longitude real,
  depth real,
  magnitude real,
  magnitude Type text,
  id text,
  locationSource text
);