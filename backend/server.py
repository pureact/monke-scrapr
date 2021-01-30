#Backend API and routing for monkeScrapr
#By:
#   Hayden Mirza
#   Kyle SP

import sqlite3
from flask import Flask
from flask import request
app = Flask(__name__)

#Create users table
userConn = sqlite3.connect('users.db')
usersTable = ''' CREATE TABLE IF NOT EXISTS USERS(
    USERNAME TEXT NOT NULL, 
    PASSWORD TEXT NOT NULL,
    EMAIL TEXT NOT NULL,
    PRIMARY KEY(EMAIL)
)'''
userCursor = userConn.cursor()
userCursor.execute(usersTable)
userConn.commit()
userConn.close()

#Default landing page
@app.route('/')
def index():
    return 'Hello world'

#TODO: Proper authentication. Only pushes data to database for now
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
        
        registerConn = sqlite3.connect('users.db')
        registerCursor = registerConn.cursor()
        registerCursor.execute("INSERT INTO USERS (username, email, password) VALUES(?,?,?)", [username, email, password])
        registerConn.commit()
        registerConn.close()
    return {}, 200

#Login user

#Logout user


app.run(debug=True, host='0.0.0.0')