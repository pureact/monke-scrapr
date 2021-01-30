#Backend API and routing for monkeScrapr
#By:
#   Hayden Mirza
#   Kyle Poirier-Szekely

import sqlite3
from dynaport.dynaport import Dynaport
from flask import Flask, request, session
from dotenv import load_dotenv
from util import generate_config
scrapr = Dynaport().get_module(name="scrapr", path="../scrapr.py")
scrapr.RedditScrapr()
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
configsTable = ''' CREATE TABLE IF NOT EXISTS CONFIGS(
    EMAIL TEXT NOT NULL, 
    CONFIG_NAME TEXT NOT NULL,
    CONFIG_PATH TEXT NOT NULL,
    PRIMARY KEY(CONFIG_PATH)
)'''
userCursor = userConn.cursor()
userCursor.execute(usersTable)
userCursor.execute(configsTable)
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

#Create config
@app.route('/createConfig', methods=['POST'])
def createConfig():
    request_data = request.get_json()

    email = session["email"]
    
    config_name = None
    if request_data:
        if 'configName' in request_data:
            config_name = request_data['configName']

        params = {"scrapr_type":"reddit", "limit":request_data.get("numPosts"), "subreddit":request_data.get("subreddit"), "sorting":request_data.get("sorting") , "keywords":request_data.get("keywords"), "tracked_users":request_data.get("trackedUsers")}
        config_path = generate_config(config_name, "configs", **params)

        configConn = sqlite3.connect('users.db')
        configCursor = configConn.cursor()
        try:
            configCursor.execute("INSERT INTO CONFIGS (EMAIL, CONFIG_NAME, CONFIG_PATH) VALUES(?,?,?)", [email, config_name, config_path])
        except:
            configConn.close()
            return {"status": 400}, 400
        configConn.commit()
        configConn.close()
    return {"status": 200}, 200

app.run(debug=True, host='0.0.0.0')