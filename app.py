from flask import Flask, render_template, request, redirect, url_for, flash
import os
import json
import random
from flask_pymongo import PyMongo

# for env.py set up
if os.path.exists("env.py"):
    import env
# bson.json converts the mongo format to json for workability
from bson.json_util import dumps, loads
from bson.objectid import ObjectId

app = Flask(__name__)

# to set the DB and the URI
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
print('Connected to:', os.environ.get("MONGO_URI"))
print('DB name:', os.environ.get("MONGO_DBNAME"))


# to set the mongo object
mongo = PyMongo(app)


@app.route('/')  # ok
def home():
    return render_template('home.template.html')


@app.route('/register')  # ok
def register():
    return render_template('register.template.html')


@app.route('/login')  # ok
def login():
    return render_template('login.template.html')

@app.route('/notfound')
def not_found():
    return render_template('item_notfound.template.html')

# display all items list - vistor view
@app.route('/browse')  # ok
def browse_items():
    items = mongo.db.items.find()
    print(items)
    return render_template('browse_items.template.html', items_stored=items)


# display all items list - login view
@app.route('/listings')  # ok
def item_list():
    items = mongo.db.items.find()
    return render_template('item_listings.template.html', all_items=items)


# view item details
@app.route('/items/<item_id>')  # ok
def view_item_details(item_id):
    item = list(mongo.db.items.find({"_id": ObjectId(item_id)}))
    print('Item selected for VIEW:', item)
    return render_template('item_details.template.html', item=item)


# add item - with ['POST']
@app.route('/items/post', methods=['POST', 'GET'])  # ok
def post_items():
    if request.method == 'POST':
        print('Form-values grab:', request.form)
        item = {
            'name': request.form.get('item_name'),
            'description': request.form.get('description'),
            'age': request.form.get('age'),
            'condition': request.form.get('condition'),
            'delete': request.form.get('delete_after'),
            'date': request.form.get('date')
        }
        mongo.db.items.insert_one(item)
        flash(f'Item "{item["name"]}" added', 'message')
        return redirect(url_for("item_list"))

    return render_template('post_item.template.html')


# edit item - with ['POST']
@app.route('/items/<item_id>/edit', methods=["GET", "POST"])  # ok
def edit_items(item_id):
    if request.method == 'POST':
        item = {
            'name': request.form.get('item_name'),
            'description': request.form.get('description'),
            'age': request.form.get('age'),
            'condition': request.form.get('condition'),
            'delete': request.form.get('delete_after')
        }
        mongo.db.items.update_one({"_id": ObjectId(item_id)}, {'$set': item})
        flash(f'Item "{item["name"]}" updated', 'info')  
        return redirect(url_for("item_list"))

    item = mongo.db.items.find_one({"_id": ObjectId(item_id)})
    return render_template('edit_item.template.html', item=item)


# delete item - with ['POST']
@app.route("/items/<item_id>/delete", methods=["GET", "POST"])  # ok
def delete_items(item_id):
    if request.method == 'POST':
        mongo.db.items.remove({"_id": ObjectId(item_id)})
        flash(f"Item deleted", 'error')
        return redirect(url_for("item_list"))

    item = list(mongo.db.items.find({"_id": ObjectId(item_id)}))
    return render_template('show_delete_item.template.html',
                           item=item)


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            # only one program can run on one port,
            # therefore flask gives error
            # if it is run 2nd time
            port=int(os.environ.get('PORT')),
            debug=True)
