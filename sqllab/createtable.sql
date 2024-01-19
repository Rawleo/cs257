DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quakeDate text, --for whatever reason timestamp with time zone works 
                  --for some people and does not work for others
  latitude real,
  longitude float,
  depth float,
  magnitude float,
  magnitudeType text,
  id text,
  locationSource text 
);

