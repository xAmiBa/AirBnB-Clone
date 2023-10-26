import os
from flask import Flask, request, render_template, redirect, url_for, session, flash
from lib.database_connection import get_flask_database_connection
from lib.Space_repository import Space_repository
from lib.Space import Space
from lib.User_repository import User_repository
from lib.User import User
from lib.request_repository import Request_repository
from lib.request import Request

from lib.Space_repository import Space_repository
from lib.Space import Space
from lib.request import Request
from lib.request_repository import Request_repository

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

    user_repository = User_repository()

    if user_repository.login_valid(username, password) == True:
        user_object = user_repository.get_user_by_username(username)
        # starts a new session
        session['username'] = username
        session['user_id'] = user_object.id
        return redirect('spaces')
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
@app.route('/spaces', methods = ['GET'])
def spaces_list():
    connection = get_flask_database_connection(app)
    space_repository = Space_repository(connection)
    lst = space_repository.all_spaces()
    return render_template('spaces.html', spaces =lst)

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
        price = float(request.form['price'])
        available_from = request.form['available_from']
        available_till = request.form['available_till']
        repository.add_space(Space(None,name, description, price, available_from, available_till, ""))
        return redirect('/spaces')

# [GET] /spaces/<id> -- template = spaces
# Returns page specific space by its' id with calendar to choose a booking date
# This is a page where user post a request
# Posts a new request for booking a space
@app.route('/spaces/<id>', methods=['GET', 'POST'])
def get_single_space(id):
    if request.method == 'GET':
        connection = get_flask_database_connection(app)

        # get space object and pass to in jinja args
        space_repository = Space_repository(connection)
        space = space_repository.search_by_id(id)

        # get available dates for the space and display dropdown calendar
        calendar = space_repository.get_dates_by_id(id)

        return render_template('single_space.html', space=space, calendar=calendar)

    if request.method == 'POST':
        connection = get_flask_database_connection(app)
        request_repository = Request_repository(connection)
        requested_date = request.form["booking_date"]
        # WARNING: TODO request_user_id must be changed to sessions["user_id"] when it works
        request_user_id = 1
        space_id = id

        # new_request false by default
        new_request = Request(None, request_user_id, space_id, requested_date, False)
        request_repository.add_request(new_request)
        message = "Thank you for your request!"

        space_repository = Space_repository(connection)
        space = space_repository.search_by_id(id)
        calendar = space_repository.get_dates_by_id(id)
        url = f"/spaces/{id}"

        return render_template('single_space.html', space=space, calendar=calendar, url=url, message=message)

'''NOT IN USE'''
# [GET][POST] /requests - template: request.html
# Returns page with all requests sent to the owner
# Posts accepted request or rejected request (availability of space changes)
# @app.route('/requests', methods=['GET'])
# @app.route('/requests', methods=['POST'])

# [GET][POST] /space/<id>/requests - template: request.html
# Returns page specific space by its' id with associated requests
# This is a page where user (ideally only owner of the space)
# Posts accepted request or rejected request (updating availability)
# @app.route('/spaces/<id>/requests', methods=['GET', 'POST])
@app.route('/spaces/<id>/requests', methods=['GET'])
def get_space_requests(id):
    connection = get_flask_database_connection(app)
    connection.connect()
    space_repo = Space_repository(connection)
    spaces = space_repo.all_spaces()

    request_repo = Request_repository(connection)
    request_list = request_repo.get_all_requests()

    space = space_repo[id-1]
    space_name = space.name

    return render_template('request.html', name=space_name, requests=request_list)


#Redirects to relevant request page
@app.route('/load_request', methods=['POST'])
def load_request():
    id = request.form['request_id']
    return redirect(f"/requests/{id}")

# @app.route('/requests/<id>', methods=['GET'])
# def get_request_details(id):
#     connection = get_flask_database_connection(app)
#     connection.connect()

#     user_repo = User_repository(connection)
#     users = user_repo.all()


#     space_repo = Space_repository(connection)
#     spaces = space_repo.all_spaces()

#     request_repo = Request_repository(connection)
#     request_list = request_repo.get_all_requests()

#     _request = request_repo[id-1]

#     space = spaces[_request.space_id-1]
#     space_name = space.name

#     _user = users[_request.request_user_id-1]

#     return render_template('request_details.html', name=space_name, date=_request.requested_date, user=_user.name)


@app.route('/requests', methods=['GET'])
def get_user_requests():
    if 'user_id' in session:
        user_id = session['user_id']
        connection = get_flask_database_connection(app)
        request_repository = Request_repository(connection)
        user_requests = request_repository.get_requests_for_user(user_id)

        return render_template('request.html', name="Your Requests", requests=user_requests)
    else:
        # Handle the case where the user is not logged in.
        # You can redirect to a login page or display a message.
        return "Please log in to view your requests."

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))