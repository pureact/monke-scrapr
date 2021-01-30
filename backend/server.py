#Backend API and routing for monkeScrapr
#By:
#   Hayden Mirza
#   Kyle SP

import sqlite3
from flask import Flask

userConn = sqlite3.connect('users.db')
app = Flask(__name__)

#Default landing page
@app.route('/')
def index():
    return 'Hello world'

#Register user

#Login user

#Logout user


app.run(debug=True, host='0.0.0.0')