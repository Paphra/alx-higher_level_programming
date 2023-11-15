-- list all records
-- don't show the records without name value
SELECT score, name FROM second_table WHERE name != '' ORDER BY score DESC;
