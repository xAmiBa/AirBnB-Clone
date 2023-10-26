import os
from flask import Flask, request, render_template, redirect, url_for
from lib.database_connection import get_flask_database_connection
from lib.Space_repository import Space_repository
from lib.Space import Space
from lib.User_repository import User_repository
from lib.User import User
from lib.request_repository import Request_repository
from lib.request import Request

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
        # request_user_id TODO: need Jake's session

        # TODO: get all data to post new request: request_user_id, space_id, requested_date, status
        # new_request = Request(None, request_user_id, id, requested_date, False)
        # request_repository.add_request(new_request)
        message = "Thank you for your request!"

        space_repository = Space_repository(connection)
        space = space_repository.search_by_id(id)
        calendar = space_repository.get_dates_by_id(id)
        url = f"/spaces/{id}"

        return render_template('single_space.html', space=space, calendar=calendar, url=url, message=message)

# WORK IN PROGRESS 
# @app.route('/spaces/<id>', methods=['POST'])
# def post_request_for_single_space(id):
    # connection = get_flask_database_connection(app)
    # request_repository = Request_repository(connection)

    # requested_date = request.form("calendar") #TODO is calendar ref id to chosen date?
    # # request_user_id TODO: need Jake's session

    # # TODO: get all data to post new request: request_user_id, space_id, requested_date, status
    # # new_request = Request(None, request_user_id, id, requested_date, False)
    # # request_repository.add_request(new_request)
    # message = "Thank you for your request!"

    # space_repository = Space_repository(connection)
    # space = space_repository.search_by_id(id)
    # calendar = space_repository.get_dates_by_id(id)
    # url = f"/spaces/{id}"

    # return render_template('single_space.html', space=space, calendar=calendar, url=url, message=message)


# [GET][POST] /requests - template: request.html
# Returns page with all requests sent to the owner
# Posts accepted request or rejected request (availability of space changes)
# @app.route('/requests', methods=['GET'])
# @app.route('/requests', methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))