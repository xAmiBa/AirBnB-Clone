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
        name_rows = self._connection.execute(
            'SELECT * from users WHERE username = %s', [user.name])
        email_rows =  self._connection.execute(
                        'SELECT * from users WHERE email = %s', [user.email])
        if name_rows == [] and email_rows == []:
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

    def generate_errors(self, user_object):
        errors = []
        
        if user_object.name == "" or user_object.name == None:
            errors.append("Name cannot be empty.")
            
        if user_object.username == "" or user_object.username == None:
            errors.append("Username cannot be empty.")
        
        if user_object.email == "" or user_object.email == None:
            errors.append("Email cannot be empty.")

        if user_object.password == "" or user_object.password == None:
            errors.append("Password cannot be empty.")
        
        if "@" not in user_object.email:
            errors.append("I doesn't look like correct email.")
        
        return errors

