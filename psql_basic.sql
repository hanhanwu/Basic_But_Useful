
-- psql looks like sql but still have some difference, need some reminder here

-- 1. match elements in timestamp, such as year, day
-- Match day from timestamp 2017-05-25 10:20:20
date_trunc('day', my_timestamp) = '2017-05-25 00:00:00';
-- Match year from timestamp 2017-05-25 10:20:20
date_trunc('year', my_timestamp) = '2017-01-01 00:00:00';


-- 2. extract elments from timestamp, such as hour, from timestamp 2017-05-25 10:20:20
extract(hour from my_timestamp)


-- read json column, in psql some columns are in JSON format and you can get access to the values through keys
json_extract_path_text(col_name, 'key1')
json_extract_path_text(json_extract_path_text(col_name, 'key1'), 'key2')


-- multiple inner join
select * from t1
inner join 
  ( select x, y from A) t2
on t1.x = t2.x
inner join
  ( select x, y from B) t3
on t1.x = t3.x
