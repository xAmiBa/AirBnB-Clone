import os
from flask import Flask, request, render_template, redirect, session, flash
from lib.database_connection import get_flask_database_connection
from lib.Space_repository import Space_repository
from lib.Space import Space
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
@app.route('/login', methods=['GET'])
def open_login():
    return render_template('login.html')

# Route for processing the login form submission
@app.route('/login', methods=['POST'])
def login():
    # Retrieve login details from the form
    username = request.form.get('username')
    password = request.form.get('password')

    new_repo = User_repository()

    if new_repo.login_valid(username, password) == True:
        # starts a new session
        session['username'] = username
        return redirect('spaces.html')
    
    else:
        flash('Invalid username or password. Please try again.')  # Store an error message
        return redirect('login') 



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
    # if there are no errors, user is added
    if user_repository.validate_new_user(new_user) == True and errors == []:
        user_repository.add_user(new_user)
        message = "Thank you, you are signed up! Now login."
        return render_template('signup.html', message=message)
    # if there are errors, we print them
    else:
        return render_template('signup.html', errors=errors)

# [GET] /spaces -- template = spaces
# Returns page with all spaces listed
# @app.route('/spaces', methods=['GET'])

# [GET][POST] /spaces/new -- template = new_place.html
# Returns page with all spaces listed
# Posts a new space listing
# @app.route('/spaces/new', methods=['GET'])
# @app.route('/spaces/new', methods=['POST'])

@app.route('/spaces/new', methods = ['GET', 'POST'])
def new_space():
    connection = get_flask_database_connection(app)
    repository = Space_repository(connection)
    if request.method == 'GET':
        space_repository = Space_repository(connection)
        lst = space_repository.all_spaces()
        return render_template('new_space.html', spaces =lst)
    elif request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        available_from = request.form['available_from']
        available_to = request.form['available_to']

        repository.add_space(Space(name, description, price, available_from, available_to))
        return redirect(f"/spaces")

# [GET] /spaces/<id> -- template = spaces
# Returns page specific space by its' id with calendar to choose a booking date
# This is a page where user post a request
# Posts a new reuest for booking a space
# @app.route('/spaces/<id>', methods=['GET'])
# @app.route('/spaces/<id>', methods=['POST'])

# [GET][POST] /requests - template: request.html
# Returns page with all requests sent to the owner
# Posts accepted request or rejected request (availability of space changes)
# @app.route('/requests', methods=['GET'])
# @app.route('/requests', methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))