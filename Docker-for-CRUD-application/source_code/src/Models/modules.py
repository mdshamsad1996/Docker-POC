from flask import json
from flask_mysqldb import MySQL
from src import app


app.config['MYSQL_HOST'] = 'mysql-container'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'shamsad@123'
app.config['MYSQL_DB'] = 'student_info'

mysql = MySQL(app) 



class Database:
    def read(self):
        cur = mysql.connection.cursor()
        try:
            cur.execute("select * from student")
            records = cur.fetchall()
            stduent_details = []

            for record in records:
                student_info = {}
                student_info['RollNo'] = record[0]
                student_info['Name'] = record[1]
                student_info['Dept'] = record[2]
                stduent_details.append(student_info)
            return stduent_details

        finally:
            cur.close()  

    def read_one_record(self,rollno):
        cur = mysql.connection.cursor()
        try:
            cur.execute("select * from student where RollNo= %s", (rollno,))
            record = cur.fetchall()
            if record :
                student_record= {}
                student_record['RollNo'] = rollno
                student_record['Name'] = record[0][1]
                student_record['Dept'] = record[0][2]
            
                return student_record
            else:
                return "Student does not exist with roll no "+str(rollno)
        
        finally:
            cur.close()  


    def insert(self,data):
        cur = mysql.connection.cursor()
        try:
            record = json.loads(data)
            cur.execute("INSERT INTO student(RollNo,Name,Dept) VALUES('%s',%s,%s)",(record['RollNo'],record['Name'],record['Dept']))
            mysql.connection.commit()
            
            return "Success"
        finally:
            cur.close()


    def update(self,rollno,data):
        cur = mysql.connection.cursor()
        try:
            record = json.loads(data)
            cur.execute("UPDATE student set Name=%s,Dept=%s where RollNo=%s",(record['Name'], record['Dept'],rollno))
            mysql.connection.commit()
            return "succes"

        finally:
            cur.close()

        
    def delete(self,rollno):
        cur = mysql.connection.cursor()
        try:
            cur.execute("Delete from student where RollNo=%s",(rollno,))
            mysql.connection.commit()
            return "sucess"
        finally:
            cur.close()
