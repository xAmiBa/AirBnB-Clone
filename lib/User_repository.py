from lib.User import User
class User_repository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from USERS')
        users = []
        for row in rows:
            item = User(row["id"], row["username"], row["name"], row["email"], row["password"])
            users.append(item)
        return users
    
    def add_user(self, user):
        rows = self._connection.execute(
            'SELECT * from users WHERE username = %s', [user.name])
        if rows == []:
            self._connection.execute('INSERT INTO users (username, name, email, password) VALUES (%s, %s, %s, %s)', [
                                user.username, user.name, user.email, user.password])
            return None
        else:
            return f"This user is alredy register"


    def login_valid(self, username, password):
        rows = self._connection.execute(
            'SELECT * from users WHERE username = %s and password = %s', [username, password])
        if rows != []:
            row = rows[0]
            valid_user = User(row["id"], row["username"], row["name"], row["email"], row["password"])
            return f"Welcome {valid_user.name}"
        else:
            return f"Username or password is not valid"