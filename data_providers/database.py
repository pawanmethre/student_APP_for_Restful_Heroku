import psycopg2

con = psycopg2.connect(database='student', user='postgres', password='108', port='5432',host='127.0.0.1')
cur = con.cursor()
create_stud_table = "CREATE TABLE students (rollno INT PRIMARY KEY NOT NULL, name TEXT NOT NULL, age INT NOT NULL, branch TEXT NOT NUll)"
cur.execute(create_stud_table)

create_user_table = "CREATE TABLE  users (username TEXT NOT NULL, password TEXT NOT NULL, email TEXT NOT NULL, role TEXT NOT NULL)"
cur.execute(create_user_table)


cur.close()
con.commit()
con.close()