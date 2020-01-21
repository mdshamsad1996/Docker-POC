use student_info;
CREATE TABLE IF NOT EXISTS student (
  RollNo INT Primary Key,
  Name varchar(40),
  Dept varchar(50)
);

INSERT INTO student (RollNo, Name, Dept) values(1,"Kartik","Mechanical");
