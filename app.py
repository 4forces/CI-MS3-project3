from flask import Flask, render_template, request, redirect, url_for, flash
import os
import json
import random


# initialise Users database
app = Flask(__name__)
usersdb = {}
with open('users.json') as fp:
    usersdb = json.load(fp)


# initialise Items dtabase
app = Flask(__name__)
itemsdb = {}
with open('items.json') as fp:
    itemsdb = json.load(fp)


# Secret key for flash messages
app = Flask(__name__)
app.secret_key = b'laksdfoi323d'

# function to save users
def save_users():
    with open('users.json', 'w') as fp:
        json.dump(usersdb, fp)

# function to save items
def save_items():
    with open('items.json', 'w') as fp:
        json.dump(itemsdb, fp)


@app.route('/')
def home():
    return render_template('home.template.html')


@app.route('/register')
def register():
    return render_template('register.template.html')


@app.route('/login')
def login():
    return render_template('login.template.html')

# browse items list
@app.route('/items/browse')
def browse_items():
    return render_template('browse_items.template.html', all_items=itemsdb)

# view single item details
@app.route('/items/<int:item_id>')
def view_item_details(item_id):
    item_to_view = None
    for each_item in itemsdb:
        if each_item["id"] == item_id:
            item_to_view = each_item
            break

    if item_to_view:
        return render_template('item_details.template.html',
                                item=item_to_view)

    else:
        return render_template('item_notfound.template.html',
                                item=item_id)


@app.route('/items/post')
def post_item():
    return render_template('post_item.template.html')


@app.route('/itms/listings')
def item_list():
    return render_template('item_listings.template.html')


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            # only one program can run on one port, therefore flask gives error if it is run 2nd time
            port=int(os.environ.get('PORT')),
            debug=True)
