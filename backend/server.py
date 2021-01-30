#Backend API and routing for monkeScrapr
#By:
#   Hayden Mirza
#   Kyle SP

import sqlite3
from flask import Flask

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

#Login user

#Logout user


app.run(debug=True, host='0.0.0.0')