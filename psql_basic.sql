
-- psql looks like sql but still have some difference, need some reminder here

-- 1. match elements in timestamp, such as year, day
-- Match day from timestamp 2017-05-25 10:20:20
date_trunc('day', my_timestamp) = '2017-05-25 00:00:00';
-- Match year from timestamp 2017-05-25 10:20:20
date_trunc('year', my_timestamp) = '2017-01-01 00:00:00';
-- select date
select my_timestamp::date from my_table;
-- extract time elements such as month, week
select extract(week from requesttime) as week from my_table;


-- 2. extract elments from timestamp, such as hour, from timestamp 2017-05-25 10:20:20
extract(hour from my_timestamp)


-- read json column, in psql some columns are in JSON format and you can get access to the values through keys
json_extract_path_text(col_name, 'key1')
json_extract_path_text(json_extract_path_text(col_name, 'key1'), 'key2')
-- read json in an array
json_extract_path_text(json_extract_array_element_text(col_name, 0), 'key1')


-- multiple inner join
-- from what I have found so far, in psql, if there is where or other clause before join clause, you may need to use () to wrap this table
select t1.x from
  (select x, z from C where....) t1
inner join 
  (select x, y from A) t2
on t1.x = t2.x
inner join
  (select x, y from B) t3
on t1.x = t3.x

-- multiple inner join
--without other clause, you can do join directly
select t1.x from
C t1
inner join 
  (select x, y from A) t2
on t1.x = t2.x
inner join
  (select x, y from B) t3
on t1.x = t3.x

-- export output to local csv
-- You'd better do this through your terminal
-- This is the best way I found that won't mess up the data when I am using Python CSV DicReader to read
PGPASSWORD=[password] psql -h [host] -U [user_name] -d [database] -p 5439 -A  -F '|' -c "select * from [table]" -o test.csv


-- When you have UNION and LIMIT
(select *
from A
limit 70000)
union
(select *
from B
limit 70000)
union
(select *
from C
limit 70000)
