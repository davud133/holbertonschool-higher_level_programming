-- creates second_table
CREATE TABLE IF NOT EXISTS second_table(
  id INT,
  name VARCHAR(256),
  score INT
);
INSERT INTO second_table
values(1, "John", 10)
values(2, "Alex", 3)
values(3, "Bob", 14)
values(4, "George", 8);
