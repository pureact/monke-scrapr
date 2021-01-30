#Backend API and routing for monkeScrapr
#By:
#   Hayden Mirza
#   Kyle SP

import sqlite3
from flask import Flask
from flask import request

userConn = sqlite3.connect('users.db')
app = Flask(__name__)

#Create users table
usersTable = ''' CREATE TABLE IF NOT EXISTS USERS(
    USERNAME TEXT NOT NULL, 
    PASSWORD TEXT NOT NULL,
    EMAIL TEXT NOT NULL,
    PRIMARY KEY(EMAIL, PASSWORD)
)'''
userCursor = userConn.cursor()
userCursor.execute(usersTable)
userConn.commit()

#Default landing page
@app.route('/')
def index():
    return 'Hello world'

#Register user
@app.route('/register', methods=['POST'])
def register():
    request_data = request.get_json()

    username = None
    email = None
    password = None

    if request_data:
        if 'username' in request_data:
            username = request_data['username']
        if 'email' in request_data:
            email = request_data['email']
        if 'password' in request_data:
            password = request_data['password']
    return '''username: {} email: {} password: {}'''.format(username, email, password)

#Login user
@app.route('/login', methods=['POST'])
def login():
    request_data = request.get_json()
    
    validUser = False
    validPass = False

    if request_data:
        if 'email' in request_data:
            validUser = True
        if 'password' in request_data:
            validPass = True
    return "validUser: {} validPass {}".format(validUser, validPass)



#Logout user
@app.route('/logout', methods=['POST'])
def logout():
 return 0

app.run(debug=True, host='0.0.0.0')