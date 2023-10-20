-- script that creates database hbtn_od_2 and user user_od_2
CREATE DATABASE IF NOT EXISTS hbtn_od_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT ALL PRIVILEGES ON *.* to 'user_0d_2'@'localhost';
