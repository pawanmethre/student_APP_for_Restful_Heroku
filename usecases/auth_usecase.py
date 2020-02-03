import jwt
import sys
sys.path.append('/home/pawan/PycharmProjects/StudentApp')
from data_providers.db_operations import execute_query

secret_key = "secret108"


# authenticating wether the user is valid or not by accessing user from jwt token
def jwt_required(token):
    try:
        # jwt.decode will throw exception if its expired or invalid else successfully fetch tuples from database
        payload = jwt.decode(token, secret_key, algorithm='HS256')
        verify_user = "SELECT * FROM users WHERE username=%s"
        row = execute_query(verify_user, payload['username'])
        return row
    except jwt.ExpiredSignatureError as e:
        return str(e)
    except:
        return "invalid signature"
