
-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS REQUESTS;
DROP SEQUENCE IF EXISTS REQUESTS_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS REQUESTS_id_seq;
CREATE TABLE REQUESTS (
    id SERIAL PRIMARY KEY,
    user_id int,
    space_id int,
    requested_date text,
    status BOOLEAN
);

-- request 1 
INSERT INTO REQUESTS (user_id int, space_id int, requested_date text, status BOOLEAN) 
VALUES (1,2,"12/12/23",FALSE);

-- request 2 
INSERT INTO REQUESTS (user_id int, space_id int, requested_date text, status BOOLEAN) 
VALUES (2,4,"03/08/23",FALSE);

-- Write file into database in terminal
-- psql -h 127.0.0.1 MAKERS_BNB < db_makers_bnb.sql
-- psql -h 127.0.0.1 MAKERS_BNB_TEST < db_makers_bnb.sql
