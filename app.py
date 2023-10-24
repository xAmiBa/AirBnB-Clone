import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection

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
# @app.route('/signup', methods=['GET'])
# @app.route('/signup', methods=['POST'])

# [GET] /spaces
# Returns page with all spaces listed
# @app.route('/spaces', methods=['GET'])

# [GET][POST] /spaces/new
# Returns page with all spaces listed
# Posts a new space listing
# @app.route('/spaces/new', methods=['GET'])
# @app.route('/spaces/new', methods=['POST'])

# [GET] /spaces/<id>
# Returns page specific space by its' id with calendar to choose a booking date
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