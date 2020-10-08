from flask import Flask, render_template, request, redirect, url_for, flash
import os
import json
import random


# initialise Users database
app = Flask(__name__)
userdb = {}
with open('users.json') as fp:
    userdb = json.load(fp)


# initialise Items dtabase
app = Flask(__name__)
itemdb = {}
with open('items.json') as fp:
    itemdb = json.load(fp)


# Secret key for flash messages
app = Flask(__name__)
app.secret_key = b'laksdfoi323d'


def save_users():
    with open('users.json', 'w') as fp:
        json.dump(userdb, fp)


def save_items():
    with open('items.json', 'w') as fp:
        json.dump(itemsdb, fp)


@app.route('/')
def home():
    return render_template('home.template.html')



# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            # only one program can run on one port, therefore flask gives error if it is run 2nd time
            port=int(os.environ.get('PORT')),
            debug=True)
