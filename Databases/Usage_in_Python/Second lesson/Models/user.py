from base_model import BaseModel
class Users(BaseModel):

    def login_user(username, password):
        conn = BaseModel.cone_db()
        cursor = conn.cursor()
        user = cursor.execute('SELECT * FROM users WHERE username=%s AND password=%s', (username, password))
        user_exists = user.fetchone()
        if user_exists:
            return user_exists
        else:
            return False
