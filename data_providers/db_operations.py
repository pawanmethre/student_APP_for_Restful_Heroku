import psycopg2
import bcrypt

def connect_database(name):
    con = psycopg2.connect(database=name, user='postgres', password='108', port='5432', host='127.0.0.1')
    cur = con.cursor()
    return cur, con

def disconnect_database(cur,con):
    con.commit()
    cur.close()
    con.close()

def execute_query(query, data):
    con = psycopg2.connect(database='student', user='postgres', password='108', port='5432', host='127.0.0.1')
    cur = con.cursor()
    cur.execute(query, data)
    try:
        row = cur.fetchone()
    except:
        row = True
    con.commit()
    cur.close()
    con.close()
    return row


def fetch_studentName_db(data):
    fetch_stud = "SELECT * FROM students WHERE rollno=%s"
    row = execute_query(fetch_stud, (data,))
    if (row):
        return {"rollno": row[0], "name": row[1], "age": row[2], "branch": row[3]}, 200
    else:
        return {"message": "rollno doesnt exists"}, 404

def add_student_db(data):
    insert_stud = "INSERT INTO students(rollno, name, age, branch) VALUES(%s,%s, %s,%s)"
    row = execute_query(insert_stud, data)
    if (row):
        return {"message": "student added successfully"}, 200

def delete_student_db(data):
    delete_stud = "DELETE FROM students WHERE rollno=%s"
    row = execute_query(delete_stud, data)
    if (row):
        return {"message": "student deleted successfully"},200

def update_student_db(data):
    update_stud_br = "UPDATE students SET branch=%s WHERE rollno=%s"
    row = execute_query(update_stud_br, data)
    if (row):
        return {"message": "student branch updated successfully"}, 200

def fetch_allStudents_db():
    con = psycopg2.connect(database='student', user='postgres', password='108', port='5432', host='127.0.0.1')
    cur = con.cursor()
    select_student = "SELECT * FROM students"
    cur.execute(select_student)
    rows = cur.fetchall()
    disconnect_database(cur, con)
    if (rows):
        l=[]
        for row in rows:
            l.append({"rollno": row[0], "name": row[1], "age": row[2], "branch": row[3]})
        return {"students": l}, 200

def register_user(data):
    insert_user = "INSERT INTO users(username, password, email, role) VALUES(%s, %s, %s, %s)"
    execute_query(insert_user, data)
    return {"message": "user added successfully"}, 201


# while signing in if user is valid return jwt token for further access
def valid_user(username, password):

    select_valid_user = "SELECT * FROM users WHERE username = %s"
    row = execute_query(select_valid_user, (username,))
    if row:
        # if username is matching the authenticate password
        byte_password = password.encode('UTF-8')
        byte_db_password = row[1].encode('UTF-8')
        user = bcrypt.checkpw(byte_password, byte_db_password)
        return user
    else:
        user = False
        return user


