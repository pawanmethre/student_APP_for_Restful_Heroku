import jwt
import psycopg2

secret_key = "secret108"

# authenticating wether the user is valid or not by accessing user from jwt token
def jwt_required(token):
    payload = jwt.decode(token, secret_key, algorithm='HS256')
    con = psycopg2.connect(database='student', user='postgres', password='108', port='5432', host='127.0.0.1')
    cur = con.cursor()
    verify_user = "SELECT * FROM users WHERE username=%s"

    cur.execute(verify_user, payload['username'])
    row = cur.fetchone()
    con.commit()
    cur.close()
    con.close()
    return row
