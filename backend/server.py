#Backend API and routing for monkeScrapr
#By:
#   Hayden Mirza
#   Kyle Poirier-Szekely

import sqlite3
from flask import Flask, request, session
from dotenv import load_dotenv
app = Flask(__name__)
load_dotenv()

import os
app.secret_key = os.environ.get("secret")

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
        try:
            registerCursor.execute("INSERT INTO USERS (username, email, password) VALUES(?,?,?)", [username, email, password])
        except:
            return {"status": 400}, 400
        registerConn.commit()
        registerConn.close()
        session['username'] = username
        session['loggedIn'] = True
    return {"status": 200}, 200

#Login user
@app.route('/login', methods=['POST'])
def login():
    request_data = request.get_json()
    status = 401
    email = None
    password = None

    if request_data:
        if 'email' in request_data:
            email = request_data['email']
        if 'password' in request_data:
            password = request_data['password']

    loginConn = sqlite3.connect('users.db')
    loginCursor = loginConn.cursor()
    loginCursor.execute("SELECT * FROM USERS WHERE email = ? AND password = ?", [email, password])

    if loginCursor.fetchone():
        status = 200

    return {"status": status, "data": {}}, status

#Logout user
@app.route('/logout', methods=['POST'])
def logout():
 return 0

app.run(debug=True, host='0.0.0.0')