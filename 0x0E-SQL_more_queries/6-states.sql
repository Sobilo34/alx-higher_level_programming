-- A script that create the database if not exists
-- states description: id INT unique, auto generated, can’t be null and is a primary key, name VARCHAR(256) can’t be null
-- If the database hbtn_0d_usa already exists, your script should not fail
-- If the table states already exists, your script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    PRIMARY KEY(id),
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL
) ENGINE=InnoDB;
