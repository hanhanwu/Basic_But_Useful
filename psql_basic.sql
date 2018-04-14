
-- psql looks like sql but still have some difference, need some reminder here

-- Create python function in psql, and in psql you can call this function
-- https://www.postgresql.org/docs/9.1/static/plpython-funcs.html

-- Check tables that you have created so that you can clean them up :)
select * from pg_tables where tableowner = '[your name in the DB system]';

-- 1. match elements in timestamp, such as year, day
-- Match day from timestamp 2017-05-25 10:20:20
date_trunc('day', my_timestamp) = '2017-05-25 00:00:00';
-- Match year from timestamp 2017-05-25 10:20:20
date_trunc('year', my_timestamp) = '2017-01-01 00:00:00';
-- select date
select my_timestamp::date from my_table;
-- extract time elements such as month, week
select extract(week from my_timestamp) as week from my_table;  -- but this one only show week # in a year, could have overlap when there are 1+ years
select date_trunc('week', my_timestamp) as week from my_table  -- this one specifys the year for the week


-- 2. extract elments from timestamp, such as hour, from timestamp 2017-05-25 10:20:20
extract(hour from my_timestamp)


-- 3. time difference
extract(day from max(my_time)-min(my_time))  -- EXTRACT days difference, you can also get hour, year differnece etc.


-- 4. Get latest n days for each group (each group may have different max date)
commit;
drop table if exists my_temp_table;
create temp table my_temp_table as
select distinct t1.col1, t2.col2, count(distinct t2.my_time) from
    (select distinct col1, max(date_trunc('day', my_time)) as max_date, dateadd(month, -6, max(date_trunc('day', my_time))) as min_date   -- latest 6 months for each group
    from my_table
    group by col1)t1
inner join
   (select distinct col1, col2, my_time
    from my_table)t2
on t1.col1 = t2.col1
and date_trunc('day', t2.my_time) <= t1.max_date
and date_trunc('day', t2.my_time) > t1.min_date
group by t1.col1, t2.col2;
commit;


-- Count number of changes along the time for each group
-- For example: a person has: red, red, red, green, green, green, purple, purple along the time, each time the color change is a change
-- and you need to count changes for each person
commit;
drop table if exists my_temp_table;
create temp table my_temp_table as
select col1, col2, my_time
from my_table
order by col1, col2;
commit;

commit;
select t3.col1, sum(t3.is_diff) as num_of_changes from
    (select t1.col1, 
    case 
        when t1.col2 <> t2.col2 then 1
        else 0
    end as is_diff
    from
    (select ROW_NUMBER() over (PARTITION BY col1 order by my_time) as r1,
    col1, col2 from my_temp_table)t1
    inner join
    (select t0.col1, t0.col2, t0.r2-1 as r2
    from (
           select ROW_NUMBER() over (PARTITION BY col1 order by my_time) as r2,
           col1, col2 from my_temp_table
           )t0
    where t0.r2 > 0
    )t2
    on t1.col1 = t2.col1
    and t1.r1 = t2.r2)t3
group by t3.col1
order by t3.col1;


-- aggregated data
select col1,
max(col2),
median(col2),
min(col2),
max(col2)-min(col2),
sum(col2)
from my_table
group by col1;


-- read json column, in psql some columns are in JSON format and you can get access to the values through keys
-- col name is important 
select json_extract_path_text(col_name, 'key1') as col1
select json_extract_path_text(json_extract_path_text(col_name, 'key1'), 'key2') as col2
-- read json in an array
select json_extract_path_text(json_extract_array_element_text(col_name, 0), 'key1') as col3


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

-- If you just want to select specific column(s) from 2+ tables, UNION may not be a good choice
-- Create a table and insert into it maybe better
drop table if exists combo_t;
create table combo_t as
select col from t1;
commit;
insert into combo_t (col)
select col from t2;
commit;


-- "Case When" to create a new column
select col1, col2,
case
  when col1 = col2 then 1,
  when col1 = col3 then 2,
  else 0
end as col3,
col4
from my_table

-- "Case When" on existing column
select col2,
case col1
  when col1 = col2 then 1,
  else 0
end,
col4
from my_table


-- order by desc on multiple cols
select * from my_table
order col1 desc, col2 desc, col3 desc, col4 desc;


-- the use of NOT IN
-- sometimes, NOT IN does not work in psql workbench, or work incorrectly
select col1 from A
where not exists (
  select col1 from B
  where A.col1 = B.col1
);

-- sometimes, NOT IN works but the above method not
select col1 frorm A
where col1 not in (select col1 from B
                  where col2 = 'x'
                  or col3 <> 'y'
                  or col4 = 'z') .  -- where there are multiple OR together, better not use AND with them in pSQL workbench
                  

-- count substring occurance (NOT apply to all types of psql)
-- case sensitive
select regexp_count(col, 'emmanuel') from my_table;


-- Choose top N rows for each group
-- In this case, choose the top 10 rows for each color, you can also order by other columns
SELECT
  * 
FROM (
  SELECT
    ROW_NUMBER() OVER (PARTITION BY color ORDER BY other_col) AS r,
    t.*
  FROM
    xxx t) x
WHERE
  x.r <= 10;  -- "<=" is very important here, since it means row_number, not number of rows

-- More complex case - control number of distinct group and make sure each group have enough records
commit;
drop table if exists my_table;
create table WF_bioscore_distribution_ipr_sample as
select * from (
    select ROW_NUMBER() over (PARTITION BY color order by my_time desc) as r,   -- order by here to choose the last N rows for each group
    t.*
    from whole_table t
    where t.my_time >= '2017-04-10'
    and t.color in 
        (select distinct color
        from whole_table
        where my_time >= '2017-04-10'
        group by color
        having count(id) >= 8  -- change the number here (this is number of rows)
        limit 1000)   -- change the number here, number of accounts
  )x
where x.r <= 8  -- change the number here (this is row number)
order by x.color, x.r;
commit;
select count(*) from my_table;

-- psql Window function. Functions such as ROW_NUMBER() are window functions
-- http://www.postgresqltutorial.com/postgresql-window-function/
LAG(), LEAD() can be used to compare current row in a group with PREVIOUS, LATER rows
There are also, LAST_VALUE(), FIRST_VALUE(), NTH_VALUE(), RANK(), DENSE_RANK(), ROW_NUMBER()

-- Using window function lag to calculate time differences between previous_time and each current time
-- date_diff(hour, prev_time, current_time), not only hour, you can calculate days differences, mins, etc.
select row_index, myid, lag(mytime) over (partition by myid, mychocolate order by mytime) as prev_time, 
mytime as current_time,
datediff(hour, lag(mytime) over (partition by myid, mychocolate order by mytime), mytime) as hour_diff
from my_table
limit 10;

-- percentile
select percentile_cont(0.05) WITHIN GROUP (ORDER BY my_val) as perct_5,
percentile_cont(0.1) WITHIN GROUP (ORDER BY my_val) as perct_10,
percentile_cont(0.25) WITHIN GROUP (ORDER BY my_val) as perct_25,
percentile_cont(0.5) WITHIN GROUP (ORDER BY my_val) as perct_50,
percentile_cont(0.75) WITHIN GROUP (ORDER BY my_val) as perct_75,
percentile_cont(0.9) WITHIN GROUP (ORDER BY my_val) as perct_90,
percentile_cont(0.95) WITHIN GROUP (ORDER BY my_val) as perct_95
from my_table;

-- Escape single quote in a string, e.g 'Emmanuel'
-- Just add a single quote before the single quote you want to escape... (I know, the logic is weird in psql)
select * from my_table
where col in (''Emmanuel'')


-- Regular expression
-- choose those with col as 10 digits, ^ outside of bracets means 'start', $ means 'end', {m} to indicate repeated number
select col form my_table
where col ~ ~ '^[0-9]{10}$';


-- drop many tables you have created
commit;
select tablename||',' from pg_tables where tableowner = '[your db username]';
-- then copy generated list
commit;
drop table if exists
[the list];
commit;


-- export data directly from workbench
-- http://www.sql-workbench.net/manual/command-export.html
WbExport -type=text
         -file='[outout file path]' -- output file path
         -delimiter='\t'
         -decimal=',';
select * from my_table LIMIT 10;
commit;
