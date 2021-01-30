#Backend API and routing for monkeScrapr
#By:
#   Hayden Mirza
#   Kyle Poirier-Szekely

import sqlite3
from flask import Flask, request, session
from dotenv import load_dotenv
from scrapr import RedditScrapr
app = Flask(__name__)
load_dotenv()

import os
app.secret_key = os.environ.get("secret")

#Create tables
tableConn = sqlite3.connect('users.db')
usersTable = ''' CREATE TABLE IF NOT EXISTS USERS(
    USERNAME TEXT NOT NULL, 
    PASSWORD TEXT NOT NULL,
    EMAIL TEXT NOT NULL,
    PRIMARY KEY(EMAIL)
)'''
configsTable = ''' CREATE TABLE IF NOT EXISTS CONFIGS(
    EMAIL TEXT NOT NULL, 
    CONFIG_NAME TEXT NOT NULL,
    CONFIG_PATH TEXT NOT NULL,
    PRIMARY KEY(CONFIG_PATH)
)'''
prawConfigsTable = ''' CREATE TABLE IF NOT EXISTS PRAWS(
    CLIENT_ID TEXT NOT NULL,
    CLIENT_SECRET TEXT NOT NULL,
    USER_AGENT TEXT NOT NULL,
    EMAIL TEXT NOT NULL,
    CONFIG_NAME TEXT NOT NULL,
    PRIMARY KEY(CONFIG_NAME, EMAIL)
)'''
tableCursor = tableConn.cursor()
tableCursor.execute(usersTable)
tableCursor.execute(configsTable)
tableCursor.execute(prawConfigsTable)
tableConn.commit()
tableConn.close()

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
            registerConn.close()
            return {"status": 400}, 400
        registerConn.commit()
        registerConn.close()
        session['email'] = email
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
        session['email'] = email
        session['loggedIn'] = True

    loginConn.close()
    return {"status": status}, status

#Logout user
@app.route('/logout', methods=['POST'])
def logout():
    if 'loggedIn' in session and session['loggedIn']:
        session.pop('email', None)
        session.pop('loggedIn', None)
        return {"status": 200}, 200
    else:
        return {"status": 400, "Error": "User not logged in."}, 400

@app.route('runRedditScraper', methods=['POST'])
def runRedditScraper():
    return 0

#Create config
@app.route('/createConfig', methods=['POST'])
def createConfig():
    request_data = request.get_json()

    email = None
    config_name = None
    config_path = None

    if request_data:
        if 'email' in request_data:
            email = request_data['email']
        if 'config_name' in request_data:
            config_name = request_data['config_name']
        if 'config_path' in request_data:
            config_path = request_data['config_path']

        configConn = sqlite3.connect('users.db')
        configCursor = configConn.cursor()
        try:
            configCursor.execute("INSERT INTO CONFIGS (EMAIL, CONFIG_NAME CONFIG_PATH) VALUES(?,?,?)", [email, config_name, config_path])
        except:
            configConn.close()
            return {"status": 400}, 400
        configConn.commit()
        configConn.close()
    return {"status": 200}, 200

app.run(debug=True, host='0.0.0.0')