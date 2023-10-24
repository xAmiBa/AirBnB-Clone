-- User stories:

-- Nouns: 

-- Column names:

-- Table name:

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

# Write file into database in terminal
psql -h 127.0.0.1 database_name < table_name.sql













