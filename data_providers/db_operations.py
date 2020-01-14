import psycopg2


def connect_database(name):
    con = psycopg2.connect(database=name, user='postgres', password='108', port='5432', host='127.0.0.1')
    cur = con.cursor()
    return cur, con

def disconnect_database(cur, con):
    con.commit()
    cur.close()
    con.close()
    return True