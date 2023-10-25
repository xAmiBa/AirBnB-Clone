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
        if name_rows == [] or email_rows == []:
            self._connection.execute('INSERT INTO users (username, name, email, password) VALUES (%s, %s, %s, %s)', [
                        user.username, user.name, user.email, user.password])
        return None
    
    # returns False if username or email already exists
    # returns True if username and email are unique
    def validate_new_user(self, user):
        name_rows = self._connection.execute(
            'SELECT * from users WHERE username = %s', [user.username])
        email_rows =  self._connection.execute(
            'SELECT * from users WHERE email = %s', [user.email])
        if name_rows == [] or email_rows == []:
            return True
        else:
            return False
    
    # returns True if username matches password in databas
    # False if not
    def login_valid(self, username, password):
        rows = self._connection.execute(
            'SELECT * from users WHERE username = %s and password = %s', [username, password])
        if rows != []:
            return True
        else:
            return False

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
            
        if self.validate_new_user(user_object) == False:
            errors.append("This email or username is alredy registered.")
        return errors

