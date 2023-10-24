
-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS <USER>;
DROP SEQUENCE IF EXISTS <table_name>_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS <table_name>_id_seq;
CREATE TABLE <table_name> (
    id SERIAL PRIMARY KEY,
    <column> text,
    <column> int,
);

INSERT INTO <table_name> (<columns>) VALUES (<values>);

-- Write file into database in terminal
-- psql -h 127.0.0.1 MAKERS_BNB < db_makers_bnb.sql
-- psql -h 127.0.0.1 MAKERS_BNB_TEST < db_makers_bnb.sql













