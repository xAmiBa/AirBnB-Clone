import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.User_repository import User_repository
from lib.User import User

# Create a new Flask app
app = Flask(__name__)

# [GET] /
# Returns the homepage
@app.route('/', methods=['GET'])
def get_homepage():
    return render_template('index.html')


#### ALL ROUTES ARE COMMENTED OUT FOR FUTURE USE, JUST UNCOMMENT TO USE
# [GET][POST] /login
# Returns the login page with login form
# Posts and validates login details to databade
# If login is validated,  creates new session
# @app.route('/login', methods=['GET'])
# @app.route('/login', methods=['POST'])

# [GET][POST] /signup
# Returns the signup page with signup form
# Posts signup details to database
@app.route('/signup', methods=['GET'])
def get_signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def post_signup():
    connection = get_flask_database_connection(app)
    user_repository = User_repository(connection)

    name = request.form['name']
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    new_user = User(None, username, name, email, password)
    errors = user_repository.generate_errors(new_user)
    # if there are errors, we print them
    if errors == []:
        return render_template('index.html')
    # if there are no errors, user is added
    else:
        user_repository.add_user(new_user)
        message = "Thank you, you are signed up! Now login."
        return render_template('signup.html', errors=errors, message=message)

# [GET] /spaces
# Returns page with all spaces listed
# @app.route('/spaces', methods=['GET'])

# [GET][POST] /spaces/new
# Returns page with all spaces listed
# Posts a new space listing
# @app.route('/spaces/new', methods=['GET'])
# @app.route('/spaces/new', methods=['POST'])

# [GET][POST] /spaces/<id>
# Returns page specific space by its' id with calendar to choose a booking date
# This is a page where user post a request
# Posts a new reuest for booking a space
# @app.route('/spaces/<id>', methods=['GET'])
# @app.route('/spaces/<id>', methods=['POST'])

# [GET][POST] /requests
# Returns page with all requests sent to the owner
# Posts accepted request or rejected request (availability of space changes)
# @app.route('/requests', methods=['GET'])
# @app.route('/requests', methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))